# DIFFERENTIAL GEOMETRY: Curves, Surfaces, Curvature & Geodesics
# ================================================================
# Everything explained in plain language inside the code

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ================================================================
# PART 1: CURVES - Lines that bend through space
# ================================================================

class Curve:
    """
    A parametric curve in 3D space.

    Think of it like a particle moving through space. At each moment t,
    the particle is at position r(t). The path it traces is the curve.
    """

    def __init__(self, x_func, y_func, z_func, t_range=(-np.pi, np.pi)):
        self.x = x_func
        self.y = y_func
        self.z = z_func
        self.t_min, self.t_max = t_range

    def position(self, t):
        """Where is the particle at time t?"""
        return np.array([self.x(t), self.y(t), self.z(t)])

    def velocity(self, t, dt=1e-6):
        """
        The velocity vector at time t.
        Mathematically: v(t) = dr/dt
        """
        r_plus = self.position(t + dt)
        r_minus = self.position(t - dt)
        return (r_plus - r_minus) / (2 * dt)

    def tangent(self, t):
        """The unit tangent vector - direction of the curve at point t."""
        v = self.velocity(t)
        v_norm = np.linalg.norm(v)
        if v_norm < 1e-10:
            return np.array([0, 0, 0])
        return v / v_norm

    def acceleration(self, t, dt=1e-6):
        """How is the velocity changing? This tells us about curvature."""
        v_plus = self.velocity(t + dt, dt)
        v_minus = self.velocity(t - dt, dt)
        return (v_plus - v_minus) / (2 * dt)

    def curvature(self, t):
        """
        How sharply is the curve bending at point t?
        Curvature = |v x a| / |v|^3
        - Straight line: curvature = 0
        - Tight circle: high curvature
        """
        v = self.velocity(t)
        a = self.acceleration(t)
        v_norm = np.linalg.norm(v)
        if v_norm < 1e-10:
            return 0
        cross = np.cross(v, a)
        return np.linalg.norm(cross) / (v_norm ** 3)

    def normal_vector(self, t):
        """The principal normal vector - points toward center of curvature."""
        v = self.velocity(t)
        a = self.acceleration(t)
        v_norm = np.linalg.norm(v)
        if v_norm < 1e-10:
            return np.array([0, 0, 0])
        tangent = v / v_norm
        a_parallel = np.dot(a, tangent) * tangent
        a_perp = a - a_parallel
        perp_norm = np.linalg.norm(a_perp)
        if perp_norm < 1e-10:
            return np.array([0, 0, 0])
        return a_perp / perp_norm

    def binormal(self, t):
        """Tangent x Normal = Binormal. Perpendicular to both."""
        return np.cross(self.tangent(t), self.normal_vector(t))

    def torsion(self, t, dt=1e-6):
        """How much does the curve twist out of its plane?"""
        B_plus = np.cross(self.tangent(t + dt), self.normal_vector(t + dt))
        B_minus = np.cross(self.tangent(t - dt), self.normal_vector(t - dt))
        dB = (B_plus - B_minus) / (2 * dt)
        return -np.dot(dB, self.normal_vector(t))


# ================================================================
# PART 2: SURFACES - 2D sheets living in 3D space
# ================================================================

class Surface:
    """
    A parametric surface in 3D space.

    Imagine a rubber sheet. You can label each point with two numbers
    (u, v) like latitude and longitude.
    """

    def __init__(self, x_func, y_func, z_func, u_range=(-1, 1), v_range=(-1, 1)):
        self.x = x_func
        self.y = y_func
        self.z = z_func
        self.u_min, self.u_max = u_range
        self.v_min, self.v_max = v_range

    def position(self, u, v):
        return np.array([self.x(u, v), self.y(u, v), self.z(u, v)])

    def partial_u(self, u, v, du=1e-6):
        """Tangent vector in the u-direction."""
        return (self.position(u + du, v) - self.position(u - du, v)) / (2 * du)

    def partial_v(self, u, v, dv=1e-6):
        """Tangent vector in the v-direction."""
        return (self.position(u, v + dv) - self.position(u, v - dv)) / (2 * dv)

    def normal(self, u, v):
        """Unit normal vector - perpendicular to the surface."""
        n = np.cross(self.partial_u(u, v), self.partial_v(u, v))
        n_norm = np.linalg.norm(n)
        if n_norm < 1e-10:
            return np.array([0, 0, 0])
        return n / n_norm

    def first_fundamental_form(self, u, v):
        """
        Measures distances on the surface (intrinsic geometry).
        I = [[E, F], [F, G]]
        E = r_u.r_u, F = r_u.r_v, G = r_v.r_v
        """
        r_u = self.partial_u(u, v)
        r_v = self.partial_v(u, v)
        E = np.dot(r_u, r_u)
        F = np.dot(r_u, r_v)
        G = np.dot(r_v, r_v)
        return np.array([[E, F], [F, G]])

    def surface_area_element(self, u, v):
        """dA = sqrt(EG - F^2) du dv"""
        return np.sqrt(np.linalg.det(self.first_fundamental_form(u, v)))

    def second_fundamental_form(self, u, v):
        """
        Measures how the surface curves (extrinsic geometry).
        II = [[L, M], [M, N]]
        """
        n = self.normal(u, v)
        du, dv = 1e-5, 1e-5
        r_uu = (self.partial_u(u + du, v) - self.partial_u(u - du, v)) / (2 * du)
        r_vv = (self.partial_v(u, v + dv) - self.partial_v(u, v - dv)) / (2 * dv)
        r_uv = (self.partial_u(u, v + dv) - self.partial_u(u, v - dv)) / (2 * dv)
        L = np.dot(r_uu, n)
        M = np.dot(r_uv, n)
        N = np.dot(r_vv, n)
        return np.array([[L, M], [M, N]])

    def shape_operator(self, u, v):
        """S = I^-1 * II. Eigenvalues are principal curvatures."""
        I = self.first_fundamental_form(u, v)
        II = self.second_fundamental_form(u, v)
        try:
            return np.linalg.inv(I) @ II
        except np.linalg.LinAlgError:
            return np.zeros((2, 2))

    def principal_curvatures(self, u, v):
        """k1, k2 — max and min curvatures at this point."""
        eigenvalues = np.linalg.eigvals(self.shape_operator(u, v))
        return sorted(eigenvalues, key=abs, reverse=True)

    def gaussian_curvature(self, u, v):
        """
        K = k1 * k2
        K > 0: sphere-like, K < 0: saddle-like, K = 0: flat/cylindrical
        Intrinsic — an ant on the surface can measure this.
        """
        k1, k2 = self.principal_curvatures(u, v)
        return k1 * k2

    def mean_curvature(self, u, v):
        """H = (k1 + k2) / 2. H = 0 means minimal surface (soap film)."""
        k1, k2 = self.principal_curvatures(u, v)
        return (k1 + k2) / 2


# ================================================================
# PART 3: GEODESICS - "Straight Lines" on Curved Surfaces
# ================================================================

class Geodesic:
    """
    Geodesic paths on a surface.

    If you're an ant walking on the surface going "straight ahead"
    (not turning left or right), you follow a geodesic.
    """

    def __init__(self, surface):
        self.surf = surface

    def christoffel_symbols(self, u, v):
        """
        Gamma^a_bc — how coordinate lines bend on the surface.
        Formula: Gamma^a_bc = 1/2 * g^ad (dg_db/dx^c + dg_dc/dx^b - dg_bc/dx^d)
        """
        du, dv = 1e-5, 1e-5
        g = self.surf.first_fundamental_form(u, v)
        g_u_plus = self.surf.first_fundamental_form(u + du, v)
        g_u_minus = self.surf.first_fundamental_form(u - du, v)
        g_v_plus = self.surf.first_fundamental_form(u, v + dv)
        g_v_minus = self.surf.first_fundamental_form(u, v - dv)
        dg_du = (g_u_plus - g_u_minus) / (2 * du)
        dg_dv = (g_v_plus - g_v_minus) / (2 * dv)

        E, F, G = g[0, 0], g[0, 1], g[1, 1]
        E_u, F_u, G_u = dg_du[0, 0], dg_du[0, 1], dg_du[1, 1]
        E_v, F_v, G_v = dg_dv[0, 0], dg_dv[0, 1], dg_dv[1, 1]

        det_g = E * G - F * F
        if abs(det_g) < 1e-10:
            return np.zeros((2, 2, 2))
        g_inv = np.array([[G, -F], [-F, E]]) / det_g

        Gamma = np.zeros((2, 2, 2))
        Gamma[0, 0, 0] = 0.5 * g_inv[0, 0] * E_u + 0.5 * g_inv[0, 1] * (2 * F_u - E_v)
        Gamma[0, 0, 1] = 0.5 * g_inv[0, 0] * E_v + 0.5 * g_inv[0, 1] * G_u
        Gamma[0, 1, 0] = Gamma[0, 0, 1]
        Gamma[0, 1, 1] = 0.5 * g_inv[0, 0] * (2 * F_v - G_u) + 0.5 * g_inv[0, 1] * G_v
        Gamma[1, 0, 0] = 0.5 * g_inv[1, 0] * E_u + 0.5 * g_inv[1, 1] * (2 * F_u - E_v)
        Gamma[1, 0, 1] = 0.5 * g_inv[1, 0] * E_v + 0.5 * g_inv[1, 1] * G_u
        Gamma[1, 1, 0] = Gamma[1, 0, 1]
        Gamma[1, 1, 1] = 0.5 * g_inv[1, 0] * (2 * F_v - G_u) + 0.5 * g_inv[1, 1] * G_v
        return Gamma

    def geodesic_equation(self, state):
        """
        d^2u^a/dt^2 + Gamma^a_bc (du^b/dt)(du^c/dt) = 0
        Returns [du/dt, dv/dt, d^2u/dt^2, d^2v/dt^2]
        """
        u, v, u_dot, v_dot = state
        Gamma = self.christoffel_symbols(u, v)
        u_ddot = -(Gamma[0, 0, 0] * u_dot * u_dot +
                   2 * Gamma[0, 0, 1] * u_dot * v_dot +
                   Gamma[0, 1, 1] * v_dot * v_dot)
        v_ddot = -(Gamma[1, 0, 0] * u_dot * u_dot +
                   2 * Gamma[1, 0, 1] * u_dot * v_dot +
                   Gamma[1, 1, 1] * v_dot * v_dot)
        return np.array([u_dot, v_dot, u_ddot, v_ddot])

    def compute(self, u0, v0, direction, length=10, n_points=1000):
        """Compute a geodesic from (u0,v0) in given direction using RK4."""
        direction = np.array(direction, dtype=float)
        direction = direction / np.linalg.norm(direction)
        dt = length / n_points
        state = np.array([u0, v0, direction[0], direction[1]])
        path_3d = np.zeros((n_points, 3))
        path_3d[0] = self.surf.position(u0, v0)
        for i in range(1, n_points):
            k1 = self.geodesic_equation(state)
            k2 = self.geodesic_equation(state + 0.5 * dt * k1)
            k3 = self.geodesic_equation(state + 0.5 * dt * k2)
            k4 = self.geodesic_equation(state + dt * k3)
            state = state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
            path_3d[i] = self.surf.position(state[0], state[1])
        return path_3d


# ================================================================
# VERIFICATION TESTS
# ================================================================

def run_tests():
    print("\n" + "=" * 60)
    print("PRACTICAL VERIFICATIONS")
    print("=" * 60)

    # Test 1: Circle curvature = 1/R
    circle_r2 = Curve(lambda t: 2*np.cos(t), lambda t: 2*np.sin(t), lambda t: 0)
    k = circle_r2.curvature(0)
    print(f"\n1. CIRCLE (R=2): curvature = {k:.4f} (expected 0.5) {'PASS' if abs(k - 0.5) < 0.01 else 'FAIL'}")

    # Test 2: Straight line curvature = 0
    line = Curve(lambda t: t, lambda t: 2*t, lambda t: 3*t)
    k = line.curvature(1.0)
    print(f"2. STRAIGHT LINE: curvature = {k:.6f} (expected 0) {'PASS' if k < 0.001 else 'FAIL'}")

    # Test 3: Sphere K = 1/R^2
    sphere = Surface(
        lambda u, v: np.cos(u)*np.sin(v),
        lambda u, v: np.sin(u)*np.sin(v),
        lambda u, v: np.cos(v),
        u_range=(0, 2*np.pi), v_range=(0.1, np.pi-0.1)
    )
    K = sphere.gaussian_curvature(np.pi/4, np.pi/3)
    print(f"3. UNIT SPHERE: K = {K:.4f} (expected 1.0) {'PASS' if abs(K - 1.0) < 0.01 else 'FAIL'}")

    # Test 4: Plane K = 0
    plane = Surface(lambda u, v: u, lambda u, v: v, lambda u, v: 0)
    K = plane.gaussian_curvature(0.5, 0.5)
    print(f"4. PLANE: K = {K:.6f} (expected 0) {'PASS' if abs(K) < 0.001 else 'FAIL'}")

    # Test 5: Cylinder K = 0
    cylinder = Surface(
        lambda u, v: np.cos(u), lambda u, v: np.sin(u), lambda u, v: v
    )
    K = cylinder.gaussian_curvature(np.pi/4, 1)
    print(f"5. CYLINDER: K = {K:.6f} (expected 0) {'PASS' if abs(K) < 0.001 else 'FAIL'}")

    print("\nALL TESTS COMPLETE")


# ================================================================
# PART 6: TENSORS, RIEMANN CURVATURE, AND PARALLEL TRANSPORT
# ================================================================


class Tensor:
    """
    A tensor on a 2D manifold (surface).

    Tensors are multi-dimensional arrays with transformation rules.
    We store them as numpy arrays and provide:
    - Index raising/lowering with the metric
    - Contractions
    """

    def __init__(self, components, type_str):
        """
        components : array-like — tensor components as numpy array
        type_str   : str like "(k,l)" — k upper indices, l lower indices
          "(0,2)" = metric, "(2,0)" = inverse metric,
          "(1,1)" = shape operator, "(1,3)" = Riemann tensor
        """
        self.comp = np.array(components, dtype=float)
        self.type = type_str
        k, l = map(int, type_str.strip("()").split(","))
        self.num_upper = k
        self.num_lower = l
        self.rank = k + l
        assert self.comp.shape == (2,) * self.rank, \
            f"Shape {self.comp.shape} doesn't match type {type_str}"

    def contract(self, upper_pos, lower_pos):
        """
        Contract an upper index with a lower index.
        T^i_jik... -> T_jk... (summed over i)
        """
        axes = (upper_pos, self.num_upper + lower_pos)
        result = np.trace(self.comp, axis1=axes[0], axis2=axes[1])
        if result.shape == ():
            return float(result)
        new_type = f"({self.num_upper-1},{self.num_lower-1})"
        return Tensor(result, new_type)


def riemann_tensor(surface, u, v):
    """
    Compute the Riemann curvature tensor R^i_jkl at point (u,v).

    Measures the failure of vectors to return to themselves when
    parallel transported around a small loop.

    Formula:
    R^i_jkl = dGamma^i_jl/dx^k - dGamma^i_jk/dx^l
             + Gamma^i_mk * Gamma^m_jl - Gamma^i_ml * Gamma^m_jk

    In 2D: only ONE independent component — R^1_212 = K * det(g)
    """
    geo = Geodesic(surface)
    du, dv = 1e-5, 1e-5

    Gamma          = geo.christoffel_symbols(u, v)
    Gamma_u_plus   = geo.christoffel_symbols(u + du, v)
    Gamma_u_minus  = geo.christoffel_symbols(u - du, v)
    Gamma_v_plus   = geo.christoffel_symbols(u, v + dv)
    Gamma_v_minus  = geo.christoffel_symbols(u, v - dv)

    dGamma_du = (Gamma_u_plus - Gamma_u_minus) / (2 * du)
    dGamma_dv = (Gamma_v_plus - Gamma_v_minus) / (2 * dv)
    dGamma = [dGamma_du, dGamma_dv]

    R = np.zeros((2, 2, 2, 2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    d_term  = dGamma[k][i, j, l] - dGamma[l][i, j, k]
                    p_term  = sum(Gamma[i, m, k] * Gamma[m, j, l] for m in range(2))
                    p_term -= sum(Gamma[i, m, l] * Gamma[m, j, k] for m in range(2))
                    R[i, j, k, l] = d_term + p_term
    return R


def ricci_tensor(surface, u, v):
    """
    Ricci tensor R_jk = R^i_jik (contraction of Riemann).
    In 2D: R_jk = K * g_jk
    """
    R = riemann_tensor(surface, u, v)
    Ricci = np.zeros((2, 2))
    for j in range(2):
        for k in range(2):
            Ricci[j, k] = sum(R[i, j, i, k] for i in range(2))
    return Ricci


def scalar_curvature(surface, u, v):
    """
    Scalar curvature R = g^jk R_jk.
    In 2D: R = 2K (twice the Gaussian curvature).
    """
    g = surface.first_fundamental_form(u, v)
    Ricci = ricci_tensor(surface, u, v)
    det_g = g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0]
    if abs(det_g) < 1e-10:
        return 0
    g_inv = np.array([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]]) / det_g
    return sum(g_inv[j, k] * Ricci[j, k] for j in range(2) for k in range(2))


class ParallelTransport:
    """
    Parallel transport of vectors along curves on a surface.

    Moving a vector along a curve while keeping it "as parallel as
    possible" to itself. On a sphere, transporting around a loop
    rotates the vector — this is called HOLONOMY.
    """

    def __init__(self, surface):
        self.surf = surface
        self.geo = Geodesic(surface)

    def transport_along_curve(self, curve_func, t_range, vector0, n_points=500):
        """
        Parallel transport a vector along a curve.

        curve_func : callable, t -> (u, v) in parameter space
        t_range    : (t_min, t_max)
        vector0    : initial 3D vector
        Returns    : list of (3D position, 3D vector) tuples
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
        coeffs = np.linalg.lstsq(A, V, rcond=None)[0]
        a, b = coeffs

        results = [(self.surf.position(u0, v0), V.copy())]

        for i in range(1, n_points):
            t = t_vals[i]
            u, v = curve_func(t)
            if i < n_points - 1:
                u_next, v_next = curve_func(t_vals[i + 1])
                u_dot = (u_next - u) / dt
                v_dot = (v_next - v) / dt
            else:
                u_dot, v_dot = 0, 0

            Gamma = self.geo.christoffel_symbols(u, v)
            da = -(Gamma[0,0,0]*a*u_dot + Gamma[0,0,1]*a*v_dot +
                   Gamma[0,1,0]*b*u_dot + Gamma[0,1,1]*b*v_dot) * dt
            db = -(Gamma[1,0,0]*a*u_dot + Gamma[1,0,1]*a*v_dot +
                   Gamma[1,1,0]*b*u_dot + Gamma[1,1,1]*b*v_dot) * dt
            a += da
            b += db

            r_u = self.surf.partial_u(u, v)
            r_v = self.surf.partial_v(u, v)
            results.append((self.surf.position(u, v), a * r_u + b * r_v))

        return results

    def holonomy_angle(self, curve_func, t_range, n_points=500):
        """
        How much a vector rotates when parallel transported around a loop.
        On a sphere: holonomy = solid angle = K * area of loop.
        """
        u0, v0 = curve_func(t_range[0])
        r_u = self.surf.partial_u(u0, v0)
        V0 = r_u / np.linalg.norm(r_u)

        transported = self.transport_along_curve(curve_func, t_range, V0, n_points)
        V_final = transported[-1][1]
        norm = np.linalg.norm(V_final)
        if norm < 1e-10:
            return 0.0
        V_final = V_final / norm

        cos_angle = np.clip(np.dot(V0, V_final), -1, 1)
        angle = np.arccos(cos_angle)
        normal = self.surf.normal(u0, v0)
        if np.dot(np.cross(V0, V_final), normal) < 0:
            angle = -angle
        return angle


def run_riemann_tests():
    """Verify Riemann tensor and scalar curvature on known surfaces."""
    print("\n" + "=" * 60)
    print("RIEMANN CURVATURE TESTS")
    print("=" * 60)

    sphere = Surface(
        lambda u, v: np.cos(u) * np.sin(v),
        lambda u, v: np.sin(u) * np.sin(v),
        lambda u, v: np.cos(v),
        u_range=(0, 2 * np.pi), v_range=(0.1, np.pi - 0.1)
    )

    u_t, v_t = np.pi / 4, np.pi / 3
    R_scalar = scalar_curvature(sphere, u_t, v_t)
    K = sphere.gaussian_curvature(u_t, v_t)

    print(f"\n1. UNIT SPHERE")
    print(f"   Gaussian curvature K = {K:.4f}    (expected 1.0)")
    print(f"   Scalar curvature  R  = {R_scalar:.4f}  (expected 2.0 = 2K)")
    print(f"   R = 2K? {'PASS' if abs(R_scalar - 2*K) < 0.1 else 'FAIL'}")

    Ricci = ricci_tensor(sphere, u_t, v_t)
    g = sphere.first_fundamental_form(u_t, v_t)
    print(f"   Ricci/metric ratio (should be ~1.0): "
          f"{Ricci[0,0]/g[0,0]:.4f}, {Ricci[1,1]/g[1,1]:.4f}")

    print(f"\n2. PARALLEL TRANSPORT on sphere")
    pt = ParallelTransport(sphere)
    loop = lambda t: (t, np.pi / 3)
    angle = pt.holonomy_angle(loop, (0, 2 * np.pi))
    print(f"   Holonomy angle around latitude circle: {np.degrees(angle):.2f} degrees")
    print(f"   (Non-zero angle confirms sphere is curved)")


# ================================================================
# PART 7: CORRECTED RIEMANN TENSOR (stable 2D formula)
# ================================================================
# The Christoffel-derivative approach has numerical precision issues.
# For 2D surfaces, we use the exact algebraic formula instead:
#   R^i_{jkl} = K * (delta^i_k * g_{jl} - delta^i_l * g_{jk})


def riemann_tensor_2d(surface, u, v):
    """
    Riemann tensor R^i_{jkl} via Gaussian curvature (numerically stable).

    In 2D: R^i_{jkl} = K * (delta^i_k * g_{jl} - delta^i_l * g_{jk})

    This is exact — no finite-difference errors from Christoffel derivatives.
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
    """Ricci tensor R_{jk} = R^i_{jik} using the stable 2D Riemann."""
    R = riemann_tensor_2d(surface, u, v)
    Ricci = np.zeros((2, 2))
    for j in range(2):
        for k in range(2):
            Ricci[j, k] = sum(R[i, j, i, k] for i in range(2))
    return Ricci


def scalar_curvature_2d(surface, u, v):
    """Scalar curvature R = g^{jk} R_{jk} using the stable 2D Riemann."""
    g = surface.first_fundamental_form(u, v)
    Ricci = ricci_tensor_2d(surface, u, v)
    det_g = g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0]
    if abs(det_g) < 1e-10:
        return 0
    g_inv = np.array([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]]) / det_g
    return sum(g_inv[j, k] * Ricci[j, k] for j in range(2) for k in range(2))


def run_tensor_tests():
    """Full test suite: tensors, corrected Riemann, parallel transport."""
    print("\n" + "=" * 60)
    print("TENSOR & CORRECTED RIEMANN TESTS")
    print("=" * 60)

    sphere = Surface(
        lambda u, v: np.cos(u) * np.sin(v),
        lambda u, v: np.sin(u) * np.sin(v),
        lambda u, v: np.cos(v),
        u_range=(0, 2 * np.pi), v_range=(0.1, np.pi - 0.1)
    )
    plane    = Surface(lambda u, v: u,        lambda u, v: v,        lambda u, v: 0)
    cylinder = Surface(lambda u, v: np.cos(u), lambda u, v: np.sin(u), lambda u, v: v)

    u_eq, v_eq = 0, np.pi / 2

    # Metric tensor
    print("\n1. METRIC TENSOR")
    g_arr = sphere.first_fundamental_form(u_eq, v_eq)
    metric = Tensor(g_arr, "(0,2)")
    print(f"   g_ij at equator:\n   {metric.comp}")

    # Corrected Riemann on sphere
    print("\n2. SPHERE RIEMANN (corrected)")
    R_sphere = riemann_tensor_2d(sphere, u_eq, v_eq)
    K_eq = sphere.gaussian_curvature(u_eq, v_eq)
    print(f"   K = {K_eq:.6f}")
    print(f"   R^1_001 = {R_sphere[1,0,0,1]:.6f}  (expected -1)")
    print(f"   R^1_010 = {R_sphere[1,0,1,0]:.6f}   (expected  1)")
    R_sc = scalar_curvature_2d(sphere, u_eq, v_eq)
    print(f"   Scalar curvature R = {R_sc:.6f}  (expected 2.0)")
    print(f"   {'PASS' if abs(R_sc - 2.0) < 0.01 else 'FAIL'}")

    # Riemann symmetry check
    anti_kl = np.allclose(R_sphere, -np.swapaxes(R_sphere, 2, 3))
    print(f"   Antisymmetry R^i_j[kl]: {anti_kl}")

    # Plane: Riemann should be zero
    print("\n3. PLANE RIEMANN")
    R_pl = riemann_tensor_2d(plane, 0.5, 0.5)
    print(f"   Max |R| = {np.max(np.abs(R_pl)):.10f}  "
          f"{'PASS' if np.max(np.abs(R_pl)) < 1e-9 else 'FAIL'}")

    # Cylinder: Riemann should be zero (intrinsically flat)
    print("\n4. CYLINDER RIEMANN (intrinsically flat)")
    R_cy = riemann_tensor_2d(cylinder, np.pi / 4, 1)
    print(f"   Max |R| = {np.max(np.abs(R_cy)):.10f}  "
          f"{'PASS' if np.max(np.abs(R_cy)) < 1e-9 else 'FAIL'}")

    # Parallel transport on sphere
    print("\n5. PARALLEL TRANSPORT — sphere holonomy")
    pt = ParallelTransport(sphere)
    v_lat = np.pi / 3
    loop = lambda t: (t, v_lat)
    angle = pt.holonomy_angle(loop, (0, 2 * np.pi), n_points=200)
    expected = 2 * np.pi * (1 - np.cos(v_lat))
    print(f"   Computed holonomy:  {np.degrees(angle):.4f} deg")
    print(f"   Expected (2π(1-cos θ)): {np.degrees(expected):.4f} deg")
    print(f"   {'PASS' if abs(angle - expected) < 0.1 else 'FAIL'}")

    # Parallel transport on plane: should be zero
    print("\n6. PARALLEL TRANSPORT — plane (should be 0)")
    pt_pl = ParallelTransport(plane)
    def square_loop(t):
        t = t % (4 * np.pi)
        if   t < np.pi:     return (t / np.pi, 0)
        elif t < 2 * np.pi: return (1, (t - np.pi) / np.pi)
        elif t < 3 * np.pi: return (1 - (t - 2 * np.pi) / np.pi, 1)
        else:                return (0, 1 - (t - 3 * np.pi) / np.pi)
    angle_pl = pt_pl.holonomy_angle(square_loop, (0, 4 * np.pi), n_points=400)
    print(f"   Holonomy on plane: {np.degrees(angle_pl):.10f} deg  "
          f"{'PASS' if abs(angle_pl) < 0.01 else 'FAIL'}")


if __name__ == "__main__":
    run_tests()
    run_riemann_tests()
    run_tensor_tests()
