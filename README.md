# Qles Lab

Some kind of FL studio but for quantum computing:sob: was made completely by AI for me, but ill leave it here cuz why not:

Quantum Learning & Engineering Lab — a local Windows desktop quantum engineering sandbox.

**To play now, double-click `Qles Lab.exe` in this folder.** Keep `_runtime` beside the EXE. No Python installation or network connection is needed for the built application. All interfaces, missions and reference pages are in English. The dark graphite/olive theme uses cream text and warm orange accents.

This is the first complete playable release, not the entire long-term quantum research curriculum. It preserves 14 engineering objectives, 9 workspace areas and 26 reference articles. Advanced unimplemented topics are listed honestly in `docs/SCOPE.md` and in the application's reference roadmap. The circuit workbench opens immediately; there is no course landing page.

## Operate the workbench

1. The application opens directly into **Circuit workbench**. Choose an objective in the compact **TARGET** strip or experiment freely.
2. Change **Wires** to 1 for the first objective. Click H in the gate palette, then click q0's wire. You can also drag a palette gate onto the wire.
3. Amplitude bars, phase dials, the complex plane, Bloch projections, probabilities, the operator matrix and depth update immediately. The objective strip displays live PASS/FAIL metrics.
4. Click an existing gate to select it. Drag it onto another wire or time column; Delete or right-click removes it. For RX/RY/RZ, change θ in the selected-component inspector. For CX/CZ/SWAP, click a control wire, then a distinct target wire.
5. Click **Measure** for finite-shot statistics. Inspect exact counts and Wilson intervals in **Exact readout**. Use the evolution timeline for intermediate states; **Theory** and **Hint** are available when requested.
6. The **Experiments** menu contains inspectable example machines. Hardware couplers can be added or removed by clicking two nodes directly on the topology.

The simulator does not punish failed attempts or require quizzes. A result that misses the target remains inspectable. Scientific assumptions stay visible.

## What works

- Direct 1–5 qubit canvas editor: gate palette drag/drop, wire placement, gate movement, control reconnection, selection, deletion, live rotation parameters, undo/redo and JSON import/export.
- Original soft sound effects for gate placement, movement, deletion, measurement and target completion; independent volume control and mute, saved between sessions.
- Visual scientific monitors: amplitude bars and phase dials, complex-plane amplitudes, reduced-state Bloch projections, operator/density heatmaps with exact-value hover, and measurement histograms.
- Complex statevectors, full unitary matrices, probabilities, reduced density matrices, entropy and Pauli expectation values.
- Z/X/Y-basis sampling of up to one million shots, reproducible RNG seeds and 95% Wilson intervals.
- Bell, GHZ, interference, Bernstein–Vazirani and two-qubit Grover examples, with inspectable evolution.
- Interactive one-qubit matrix/vector laboratory with real and imaginary amplitude controls and explicit normalization.
- Editable two-qubit Pauli Hamiltonians, eigensystems, time evolution and a 25×25 grid VQE experiment.
- Editable hardware connectivity, heuristic SWAP routing, native-CX decomposition, adjacent gate optimization and full-unitary equivalence checks.
- Density-matrix Kraus channels: bit flip, phase flip, nonidentity-Pauli depolarizing noise, amplitude damping, T1/T2 memory and classical readout flips.
- Exact X-only repetition demo and binomial majority curve.
- Real Stim repetition and rotated surface X/Z memory experiments, decoded with PyMatching MWPM. Comparisons use the same sampled histories; failures and correction edges are inspectable.
- A clearly labeled educational FTQC resource budget with error, area, time and decoder-throughput constraints.
- QEC parameter sweeps with cancellation after a point, saved hypotheses, confidence plots, CSV and JSON exports.
- An internal reference with definitions, symbol explanations, derivations, experiments, caveats and external sources.
- Automatic atomic saves of progress, circuit, lab settings, discovered concepts and research experiments.

## Windows development commands

Run these commands in PowerShell from the project folder. Use Python 3.12 x64 to reproduce the checked build.

```powershell
cd "C:\Users\radiu\Documents\Qles Lab"
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.lock.txt
```

The existing `.venv` is already installed on this machine. Its Python was created from the Codex-bundled Python runtime; you do not need to recreate it to run source or tests here.

Run the source application:

```powershell
.\.venv\Scripts\python.exe run.py
```

Run scientific and UI tests:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Build the root-folder EXE:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build.ps1
```

Launch the built application:

```powershell
& ".\Qles Lab.exe"
```

Verify the packaged UI and render screenshots without altering your progress:

```powershell
& ".\Qles Lab.exe" --smoke-test --data-dir artifacts\packaged-smoke-data --screenshot-dir artifacts\packaged-screenshots
```

For compatible current dependency versions instead of the exact checked lock, use `requirements.txt`. `Install.bat` and `Launch Qles Lab.bat` provide shortcuts. The EXE is a directory-based build: `_runtime` is required. It has no installer, telemetry, login, cloud sync or update checker.

## Saved data and controls

The default save is `data/progress.json` beside the root-folder EXE or source project. Writes use a temporary file and atomic replacement. If an invalid save is detected, its bytes are preserved in `data/progress.corrupt.json`. Use **Export progress** for a portable backup. Closing while a background experiment is running waits for you to stop it or let it finish.

- **F5**: run the current lab.
- **Ctrl+S**: save all current configurations.
- **Ctrl+Z**: undo the last circuit edit.
- **Text** selector: adjust interface text size; pages can scroll at smaller window sizes.
- **Sound** button: mute/unmute effects. The slider changes only the application's effect volume. Default volume is 35%.
- **Files** in Circuit: export/import a circuit JSON.
- **Esc** in Circuit: return from placement to selection.
- **Delete / right-click** a canvas gate: remove it. All circuit edits can be undone.
- **Export CSV + JSON** in Research: export numerical rows and full metadata.

Conventions and scientific limitations are in `docs/SCIENCE.md`. Engineering layout is in `docs/ARCHITECTURE.md`. Validation evidence is in `docs/VALIDATION.md` and `artifacts/test-results.xml`. Tests passing does not imply the application is bug-free.
