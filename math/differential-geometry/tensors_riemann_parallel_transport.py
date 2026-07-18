"""
TENSORS, RIEMANN CURVATURE, AND PARALLEL TRANSPORT
================================================================

This module extends the differential geometry framework with:
- Tensor operations (index raising/lowering, contraction)
- Riemann curvature tensor
- Ricci tensor and scalar curvature
- Parallel transport of vectors along curves
- Holonomy (rotation of vectors around closed loops)
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Tensor:
    """
    A tensor on a 2D manifold (surface).

    Tensors are multi-dimensional arrays with transformation rules.
    We store them as numpy arrays and provide operations:
    - Index raising/lowering with the metric
    - Tensor products
    - Contractions
    """

    def __init__(self, components, type_str):
        """
        Create a tensor.

        Parameters:
        -----------
        components : array-like
            The tensor components as a numpy array
        type_str : str
            Type as "(k,l)" meaning k upper, l lower indices
            Examples: "(0,2)" = covariant 2-tensor (metric)
                      "(2,0)" = contravariant 2-tensor (inverse metric)
                      "(1,1)" = mixed tensor (shape operator)
                      "(1,3)" = Riemann tensor
        """
        self.comp = np.array(components, dtype=float)
        self.type = type_str

        # Parse type
        k, l = map(int, type_str.strip("()").split(","))
        self.num_upper = k
        self.num_lower = l
        self.rank = k + l

        assert self.comp.shape == (2,) * self.rank, \
            f"Shape {self.comp.shape} doesn't match type {type_str}"

    def __repr__(self):
        return f"Tensor{self.type}\n{self.comp}"

    def raise_index(self, metric_inv, pos):
        """
        Raise a lower index using the inverse metric.

        g^ia T_ajk... = T^i_jk...
        """
        if self.num_lower == 0:
            raise ValueError("Cannot raise index: no lower indices")

        # Contract metric_inv with the specified lower index
        new_shape = (2,) * (self.rank)
        result = np.zeros(new_shape)

        letters = 'ijklmnopqrstuvwxyz'
        metric_idx = letters[0:2]
        tensor_idx = list(letters[2:2+self.rank])

        raised_idx = tensor_idx[self.num_upper + pos]
        tensor_idx[self.num_upper + pos] = metric_idx[0]

        output_idx = tensor_idx.copy()
        output_idx[self.num_upper + pos] = metric_idx[1]

        ein_str = f"{metric_idx[0]}{metric_idx[1]},{''.join(tensor_idx)}->{''.join(output_idx)}"

        result = np.einsum(ein_str, metric_inv, self.comp)

        new_type = f"({self.num_upper+1},{self.num_lower-1})"
        return Tensor(result, new_type)

    def lower_index(self, metric, pos):
        """
        Lower an upper index using the metric.

        g_ia T^ajk... = T_i^jk...
        """
        if self.num_upper == 0:
            raise ValueError("Cannot lower index: no upper indices")

        letters = 'ijklmnopqrstuvwxyz'
        metric_idx = letters[0:2]
        tensor_idx = list(letters[2:2+self.rank])

        lowered_idx = tensor_idx[pos]
        tensor_idx[pos] = metric_idx[0]

        output_idx = tensor_idx.copy()
        output_idx[pos] = metric_idx[1]

        ein_str = f"{metric_idx[0]}{metric_idx[1]},{''.join(tensor_idx)}->{''.join(output_idx)}"

        result = np.einsum(ein_str, metric, self.comp)

        new_type = f"({self.num_upper-1},{self.num_lower+1})"
        return Tensor(result, new_type)

    def contract(self, upper_pos, lower_pos):
        """
        Contract an upper index with a lower index.

        T^i_jik... = T_jk... (summed over i)
        """
        if upper_pos >= self.num_upper or lower_pos >= self.num_lower:
            raise ValueError("Invalid contraction positions")

        axes = (upper_pos, self.num_upper + lower_pos)
        result = np.trace(self.comp, axis1=axes[0], axis2=axes[1])

        if result.shape == ():
            return float(result)

        new_type = f"({self.num_upper-1},{self.num_lower-1})"
        return Tensor(result, new_type)


def riemann_tensor_2d(surface, u, v):
    """
    Compute Riemann tensor R^i_{jkl} for a 2D surface.

    In 2D, the Riemann tensor has only one independent component.
    The formula is:
    R^i_{jkl} = K * (delta^i_k * g_{jl} - delta^i_l * g_{jk})

    where K is Gaussian curvature and g is the metric.

    This measures how vectors rotate when parallel transported
    around small loops. It captures ALL curvature information.
    """
    K = surface.gaussian_curvature(u, v)
    g = surface.first_fundamental_form(u, v)

    R = np.zeros((2, 2, 2, 2))

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    delta_ik = 1.0 if i == k else 0.0
                    delta_il = 1.0 if i == l else 0.0
                    R[i, j, k, l] = K * (delta_ik * g[j, l] - delta_il * g[j, k])

    return R


def ricci_tensor_2d(surface, u, v):
    """
    Ricci tensor R_{jk} = R^i_{jik} (contraction of Riemann).

    The Ricci tensor measures how volumes change under the metric.
    In 2D: R_{jk} = K * g_{jk} (Gaussian curvature times metric)
    """
    R = riemann_tensor_2d(surface, u, v)
    Ricci = np.zeros((2, 2))
    for j in range(2):
        for k in range(2):
            Ricci[j, k] = sum(R[i, j, i, k] for i in range(2))
    return Ricci


def scalar_curvature_2d(surface, u, v):
    """
    Scalar curvature R = g^{jk} R_{jk}.

    In 2D: R = 2K (twice the Gaussian curvature)
    """
    g = surface.first_fundamental_form(u, v)
    Ricci = ricci_tensor_2d(surface, u, v)

    det_g = g[0,0]*g[1,1] - g[0,1]*g[1,0]
    if abs(det_g) < 1e-10:
        return 0

    g_inv = np.array([[g[1,1], -g[0,1]], [-g[1,0], g[0,0]]]) / det_g

    R = sum(g_inv[j, k] * Ricci[j, k] for j in range(2) for k in range(2))
    return R


class ParallelTransport:
    """
    Parallel transport of vectors along curves on a surface.

    When you move a vector along a curve on a curved surface, you need
    to "rotate" it to keep it "parallel" to itself.

    Key insight: A vector is parallel transported if its covariant
    derivative along the curve is zero.

    On a sphere: parallel transport around a loop rotates the vector!
    This is called HOLONOMY and equals the solid angle enclosed.
    """

    def __init__(self, surface):
        self.surf = surface
        from differential_geometry import Geodesic
        self.geo = Geodesic(surface)

    def transport_along_curve(self, curve_func, t_range, vector0, n_points=500):
        """
        Parallel transport a vector along a curve.

        Parameters:
        -----------
        curve_func : callable
            Function t -> (u, v) giving the curve in parameter space
        t_range : tuple
            (t_min, t_max) range for the curve
        vector0 : array-like
            Initial vector (in 3D) to transport
        n_points : int
            Number of integration steps

        Returns:
        --------
        list of (position, vector) tuples along the curve
        """
        t_vals = np.linspace(t_range[0], t_range[1], n_points)
        dt = (t_range[1] - t_range[0]) / n_points

        u0, v0 = curve_func(t_vals[0])
        r_u = self.surf.partial_u(u0, v0)
        r_v = self.surf.partial_v(u0, v0)
        normal = self.surf.normal(u0, v0)

        V = np.array(vector0, dtype=float)
        V = V - np.dot(V, normal) * normal

        A = np.column_stack([r_u, r_v])
        try:
            coeffs = np.linalg.lstsq(A, V, rcond=None)[0]
        except:
            coeffs = np.array([0, 0])

        a, b = coeffs

        results = [(self.surf.position(u0, v0), V.copy())]

        for i in range(1, n_points):
            t = t_vals[i]
            u, v = curve_func(t)

            if i < n_points - 1:
                u_next, v_next = curve_func(t_vals[i+1])
                u_dot = (u_next - u) / dt
                v_dot = (v_next - v) / dt
            else:
                u_dot, v_dot = 0, 0

            Gamma = self.geo.christoffel_symbols(u, v)

            da = -(Gamma[0, 0, 0] * a * u_dot + Gamma[0, 0, 1] * a * v_dot +
                   Gamma[0, 1, 0] * b * u_dot + Gamma[0, 1, 1] * b * v_dot) * dt
            db = -(Gamma[1, 0, 0] * a * u_dot + Gamma[1, 0, 1] * a * v_dot +
                   Gamma[1, 1, 0] * b * u_dot + Gamma[1, 1, 1] * b * v_dot) * dt

            a += da
            b += db

            r_u = self.surf.partial_u(u, v)
            r_v = self.surf.partial_v(u, v)
            V_new = a * r_u + b * r_v

            results.append((self.surf.position(u, v), V_new))

        return results

    def holonomy_angle(self, curve_func, t_range, n_points=500):
        """
        Compute the holonomy angle: how much a vector rotates when
        parallel transported around a closed loop.

        For a small loop around a point: holonomy ~ K * area
        On a sphere: holonomy = solid angle enclosed by the loop
        """
        u0, v0 = curve_func(t_range[0])
        r_u = self.surf.partial_u(u0, v0)
        r_v = self.surf.partial_v(u0, v0)

        V0 = r_u / np.linalg.norm(r_u)

        transported = self.transport_along_curve(curve_func, t_range, V0, n_points)

        V_final = transported[-1][1]
        V_final = V_final / np.linalg.norm(V_final)

        cos_angle = np.dot(V0, V_final)
        cos_angle = np.clip(cos_angle, -1, 1)
        angle = np.arccos(cos_angle)

        normal = self.surf.normal(u0, v0)
        cross = np.cross(V0, V_final)
        if np.dot(cross, normal) < 0:
            angle = -angle

        return angle


# Example usage
if __name__ == "__main__":
    from differential_geometry import Surface

    # Create a sphere
    sphere = Surface(
        lambda u, v: np.cos(u) * np.sin(v),
        lambda u, v: np.sin(u) * np.sin(v),
        lambda u, v: np.cos(v),
        u_range=(0, 2*np.pi),
        v_range=(0.1, np.pi - 0.1)
    )

    # Compute Riemann tensor at equator
    R = riemann_tensor_2d(sphere, 0, np.pi/2)
    print("Riemann tensor at equator:")
    print(f"R^1_010 = {R[1, 0, 1, 0]:.6f}")

    # Compute scalar curvature
    R_scalar = scalar_curvature_2d(sphere, 0, np.pi/2)
    print(f"Scalar curvature R = {R_scalar:.6f}")
    print(f"Expected R = 2K = 2 for unit sphere")

    # Parallel transport
    transport = ParallelTransport(sphere)

    def latitude_circle(t):
        return (t, np.pi/3)

    angle = transport.holonomy_angle(latitude_circle, (0, 2*np.pi))
    print(f"\nHolonomy angle: {np.degrees(angle):.2f} degrees")
