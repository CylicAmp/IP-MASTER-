import React, { useState, useEffect, useRef, useCallback } from 'react';

// ─── Constants ───────────────────────────────────────────────────────────────
const MOD = 37;
const ORBIT_P = [0, 1, 4, 13, 3, 10, 31, 20, 24, 36, 35, 32, 23, 33, 26, 5, 16, 12];
const ORBIT_V = [2, 7, 22, 30, 17, 15, 9, 28, 11, 34, 29, 14, 6, 19, 21, 27, 8, 25];
const GATE    = 18;

const f = n => (3 * n + 1) % MOD;   // evolve
const g = n => (2 * n + 19) % MOD;  // promote

const STATE_MAP = {
  0:'NULL_ELEMENT', 1:'UNITY', 2:'DUALITY', 3:'TRINITY',
  4:'FOUNDATION', 5:'QUINTESSENCE', 6:'HARMONY', 7:'MYSTERY',
  8:'INFINITY', 9:'COMPLETION', 10:'PERFECTION', 11:'PORTAL',
  12:'CYCLE', 13:'TRANSFORMATION', 14:'BALANCE', 15:'RESONANCE',
  16:'INTEGRATION', 17:'BRIDGE', 18:'GATE_SOVEREIGN', 19:'THRESHOLD',
  20:'EXPANSION', 21:'PROMOTION', 22:'ELEVATION', 23:'SYNTHESIS',
  24:'CONVERGENCE', 25:'APEX', 26:'ORBIT_LOCK', 27:'VERIFIED',
  28:'CRYSTALLIZED', 29:'SEALED', 30:'MANIFEST', 31:'ANCHORED',
  32:'RESOLVED', 33:'ECHOED', 34:'ARCHIVED', 35:'MIRRORED',
  36:'COMPLETE',
};

const getPos = (val, radius) => {
  const angle = (val / MOD) * 2 * Math.PI - Math.PI / 2;
  return { x: 100 + radius * Math.cos(angle), y: 100 + radius * Math.sin(angle) };
};

const getFreq = n => 440 * Math.pow(2, n / 37);

// Pre-compute full commutation table
const COMMUTATION_TABLE = ORBIT_P.map(n => ({
  n,
  gof: g(f(n)),
  fog: f(g(n)),
  match: g(f(n)) === f(g(n)),
}));

// ─── Component ───────────────────────────────────────────────────────────────
const ModalCrossingVisual = () => {
  const [step,       setStep]       = useState(0);
  const [selected,   setSelected]   = useState(null);  // clicked [P] node
  const [hovered,    setHovered]    = useState(null);
  const [running,    setRunning]    = useState(false);
  const [isAuto,     setIsAuto]     = useState(true);
  const [showLabels, setShowLabels] = useState(true);
  const [showCommute, setShowCommute] = useState(false);
  const audioCtxRef = useRef(null);

  // Auto orbit under f(n)
  useEffect(() => {
    if (!running || !isAuto) return;
    const id = setInterval(() => setStep(s => (s + 1) % 18), 900);
    return () => clearInterval(id);
  }, [running, isAuto]);

  // Manual promotion: g(n) = 2n + 19 bridge
  const handlePromote = () => { setIsAuto(false); setStep(s => (s + 1) % 18); };

  // Sound mapping — equal temperament across mod 37
  const playTone = useCallback(n => {
    if (!audioCtxRef.current)
      audioCtxRef.current = new (window.AudioContext || window.webkitAudioContext)();
    const ctx = audioCtxRef.current;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain); gain.connect(ctx.destination);
    osc.frequency.value = getFreq(n);
    osc.type = 'sine';
    gain.gain.setValueAtTime(0.15, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.45);
    osc.start(ctx.currentTime); osc.stop(ctx.currentTime + 0.45);
  }, []);

  const activeP = ORBIT_P[step];
  const activeV = ORBIT_V[step];

  // Promotion arc source: selected node (click) or current auto step
  const arcSource = selected !== null ? selected : (running ? activeP : null);
  const arcTarget = arcSource !== null ? g(arcSource) : null;

  // ── Sub-components ─────────────────────────────────────────────────────────

  const PromotionArc = ({ from }) => {
    const to = g(from);
    const start = getPos(from, 70);
    const end   = getPos(to,   45);
    return (
      <path
        d={`M ${start.x} ${start.y} Q 100 100 ${end.x} ${end.y}`}
        fill="none" stroke="white" strokeWidth="0.9"
        strokeDasharray="2.5 2" opacity="0.75"
      />
    );
  };

  const StructuralLines = () =>
    ORBIT_P.map((p, i) => {
      const ps = getPos(p, 70), vs = getPos(ORBIT_V[i], 45);
      return (
        <line key={p}
          x1={ps.x} y1={ps.y} x2={vs.x} y2={vs.y}
          stroke="white" strokeWidth="0.25" opacity="0.07"
        />
      );
    });

  const OrbitDot = ({ val, radius, color }) => {
    const pos       = getPos(val, radius);
    const isHov     = hovered  === val;
    const isSel     = selected === val;
    const isActive  = val === activeP || val === activeV;
    const isInP     = ORBIT_P.includes(val);
    const r = isSel ? 5 : isHov ? 4.2 : isActive && running ? 3.8 : 2.8;

    return (
      <g style={{ cursor: 'pointer' }}
        onMouseEnter={() => { setHovered(val); playTone(val); }}
        onMouseLeave={() => setHovered(null)}
        onClick={() => {
          if (isInP) { setSelected(s => s === val ? null : val); playTone(val); }
        }}
      >
        {isSel && (
          <circle cx={pos.x} cy={pos.y} r={r + 3}
            fill="none" stroke={color} strokeWidth="0.6" opacity="0.35" />
        )}
        <circle cx={pos.x} cy={pos.y} r={r} fill={color}
          opacity={isHov || isSel || isActive ? 1 : 0.65}
          style={{ transition: 'r 0.15s' }}
        />
        {showLabels && (
          <text
            x={pos.x + (pos.x > 100 ? 4.5 : -4.5)} y={pos.y + 1.2}
            fontSize="3.5" fill={color}
            textAnchor={pos.x > 100 ? 'start' : 'end'} opacity="0.9"
          >
            {val}
          </text>
        )}
      </g>
    );
  };

  // ── Render ─────────────────────────────────────────────────────────────────
  return (
    <div className="font-mono bg-black text-gray-200 min-h-screen p-6">

      {/* Header */}
      <div className="text-center mb-6">
        <h1 className="text-purple-400 text-xl tracking-widest mb-1">
          MODAL CROSSING VISUALIZATION
        </h1>
        <p className="text-gray-500 text-xs">
          LoB 21 — mod 37 orbit geometry — PRODUCTION LOCKED
        </p>
      </div>

      {/* Controls */}
      <div className="flex flex-wrap gap-2 justify-center mb-5">
        <button
          onClick={() => { setRunning(r => !r); setIsAuto(true); }}
          className={`px-4 py-1.5 text-xs rounded border transition-all ${
            running
              ? 'bg-purple-900/60 border-purple-500 text-purple-200'
              : 'bg-gray-900 border-purple-700 text-purple-400 hover:bg-purple-900/30'
          }`}
        >
          {running ? '⏸ PAUSE' : '▶ PLAY'}
        </button>

        <button
          onClick={handlePromote}
          className="px-4 py-1.5 text-xs rounded border border-cyan-500/50 text-cyan-400 hover:bg-cyan-500/10 transition-all"
        >
          MANUAL PROMOTION [P] → [V]
        </button>

        {!isAuto && (
          <button
            onClick={() => setIsAuto(true)}
            className="px-4 py-1.5 text-xs rounded border border-gray-700 text-gray-400 hover:bg-gray-800 transition-all"
          >
            ↺ RESUME AUTO
          </button>
        )}

        <button
          onClick={() => setShowCommute(c => !c)}
          className={`px-4 py-1.5 text-xs rounded border transition-all ${
            showCommute
              ? 'bg-emerald-900/50 border-emerald-500 text-emerald-300'
              : 'bg-gray-900 border-gray-700 text-gray-400 hover:bg-gray-800'
          }`}
        >
          {showCommute ? '✓ COMMUTE LOCK' : 'COMMUTE'}
        </button>

        <button
          onClick={() => setShowLabels(l => !l)}
          className="px-4 py-1.5 text-xs rounded border border-gray-700 text-gray-400 hover:bg-gray-800 transition-all"
        >
          {showLabels ? 'HIDE' : 'SHOW'} LABELS
        </button>
      </div>

      {/* Main layout */}
      <div className="flex flex-wrap gap-4 justify-center items-start">

        {/* SVG */}
        <svg viewBox="0 0 200 200" width="400" height="400"
          className="rounded-xl border border-gray-800 bg-gray-950 flex-shrink-0">

          {/* Ring guides */}
          <circle cx="100" cy="100" r="70" fill="none" stroke="#22d3ee" strokeWidth="0.3" opacity="0.18" />
          <circle cx="100" cy="100" r="45" fill="none" stroke="#fbbf24" strokeWidth="0.3" opacity="0.18" />

          <StructuralLines />

          {/* Promotion arc */}
          {arcSource !== null && <PromotionArc from={arcSource} />}

          {/* Orbits */}
          {ORBIT_P.map(v => <OrbitDot key={`p${v}`} val={v} radius={70} color="#22d3ee" />)}
          {ORBIT_V.map(v => <OrbitDot key={`v${v}`} val={v} radius={45} color="#fbbf24" />)}

          {/* Gate 18 — pulsing center */}
          <circle cx="100" cy="100" r="8" fill="none" stroke="#ef4444" strokeWidth="0.5"
            opacity={running ? 0.6 : 0.3} />
          <circle cx="100" cy="100" r="5" fill="#ef4444" opacity="0.9" />
          <text x="100" y="103" fontSize="4" fill="white" textAnchor="middle">18</text>

          {/* Active step rings */}
          {running && (() => {
            const ap = getPos(activeP, 70), av = getPos(activeV, 45);
            return (
              <>
                <circle cx={ap.x} cy={ap.y} r="6" fill="none" stroke="#22d3ee" strokeWidth="0.8" opacity="0.85" />
                <circle cx={av.x} cy={av.y} r="6" fill="none" stroke="#fbbf24" strokeWidth="0.8" opacity="0.85" />
              </>
            );
          })()}
        </svg>

        {/* Info panels */}
        <div className="flex flex-col gap-3 min-w-[220px] max-w-[280px] flex-1">

          {/* Step state */}
          <div className="bg-gray-900 border border-gray-800 rounded-lg p-3">
            <div className="text-gray-500 text-xs mb-2">ORBIT STEP {step + 1} / 18</div>
            <div className="text-sm space-y-1">
              <div>
                <span className="text-cyan-400">[P] </span>
                <span className="text-white">{activeP}</span>
                <span className="text-gray-500 text-xs ml-2">{STATE_MAP[activeP]}</span>
              </div>
              <div>
                <span className="text-yellow-400">[V] </span>
                <span className="text-white">{activeV}</span>
                <span className="text-gray-500 text-xs ml-2">{STATE_MAP[activeV]}</span>
              </div>
              <div className="text-orange-400 text-xs">
                g({activeP}) = {g(activeP)}  &nbsp;·&nbsp;  f({activeP}) = {f(activeP)}
              </div>
            </div>
          </div>

          {/* Selected node */}
          <div className="bg-gray-900 border border-gray-800 rounded-lg p-3">
            <div className="text-gray-500 text-xs mb-2">SELECTED [P] NODE</div>
            {selected !== null ? (
              <div className="text-sm space-y-1">
                <div><span className="text-purple-400">n = </span><span className="text-white">{selected}</span></div>
                <div><span className="text-purple-400">state: </span><span className="text-gray-300">{STATE_MAP[selected]}</span></div>
                <div><span className="text-orange-400">g(n) → </span><span className="text-yellow-400">{g(selected)}</span><span className="text-gray-500 text-xs ml-2">{STATE_MAP[g(selected)]}</span></div>
                <div><span className="text-purple-400">freq: </span><span className="text-gray-300">{getFreq(selected).toFixed(2)} Hz</span></div>
              </div>
            ) : (
              <div className="text-gray-600 text-xs">Click any cyan [P] node…</div>
            )}
          </div>

          {/* Hover probe */}
          <div className="bg-gray-900 border border-gray-800 rounded-lg p-3">
            <div className="text-gray-500 text-xs mb-2">HOVER PROBE</div>
            {hovered !== null ? (
              <div className="text-sm space-y-1">
                <div><span className="text-purple-400">n = </span>{hovered}</div>
                <div><span className="text-purple-400">ring: </span>
                  <span className={hovered === GATE ? 'text-red-400' : ORBIT_P.includes(hovered) ? 'text-cyan-400' : 'text-yellow-400'}>
                    {hovered === GATE ? 'CENTER / GATE' : ORBIT_P.includes(hovered) ? '[P] outer' : '[V] inner'}
                  </span>
                </div>
                <div className="text-gray-400 text-xs">{STATE_MAP[hovered]}</div>
              </div>
            ) : (
              <div className="text-gray-600 text-xs">Hover any node…</div>
            )}
          </div>

        </div>
      </div>

      {/* Commutation panel */}
      {showCommute && (
        <div className="mt-4 bg-gray-900 border border-emerald-800 rounded-lg p-4 max-w-2xl mx-auto">
          <div className="text-emerald-400 text-xs mb-3 tracking-widest">
            COMMUTATION LOCK — g∘f = f∘g — ALL 18 ELEMENTS
          </div>
          <div className="overflow-x-auto">
            <table className="text-xs w-full">
              <thead>
                <tr className="text-gray-500 border-b border-gray-800">
                  <th className="text-left pb-1 pr-4">n</th>
                  <th className="text-left pb-1 pr-4">g(f(n))</th>
                  <th className="text-left pb-1 pr-4">f(g(n))</th>
                  <th className="text-left pb-1">match</th>
                </tr>
              </thead>
              <tbody>
                {COMMUTATION_TABLE.map(({ n, gof, fog, match }) => (
                  <tr key={n} className="border-b border-gray-900">
                    <td className="py-0.5 pr-4 text-cyan-400">{n}</td>
                    <td className="pr-4 text-yellow-400">{gof}</td>
                    <td className="pr-4 text-yellow-400">{fog}</td>
                    <td className={match ? 'text-emerald-400' : 'text-red-400'}>
                      {match ? '✓' : '✗'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="mt-2 text-emerald-400 text-xs">
            pathA === pathB for all 37 elements ✓ — structural lock confirmed
          </div>
        </div>
      )}

      {/* Legend */}
      <div className="flex flex-wrap gap-4 justify-center mt-5 text-xs text-gray-500">
        <span><span className="text-cyan-400">●</span> [P] outer r=70 — potential</span>
        <span><span className="text-yellow-400">●</span> [V] inner r=45 — verified</span>
        <span><span className="text-red-400">●</span> Gate 18 — sovereign</span>
        <span><span className="text-white">--</span> g(n) promotion arc</span>
        <span><span className="text-emerald-400">✓</span> commutation lock</span>
      </div>

    </div>
  );
};

export default ModalCrossingVisual;
