# AI Copilot Instructions — Data Science 2.0

Purpose: quick, actionable guidance so an AI coding agent is productive immediately in this repo.

1) Big picture
- Minimal, single-script data-science repo. The runtime entrypoint is `test.py` at project root.
- Development happens inside the isolated `.venv` (Windows paths). No services, DBs, or microservices.

2) Environment & run commands (Windows)
- Activate PowerShell:

```powershell
.venv\Scripts\Activate.ps1
.venv\Scripts\python.exe test.py
```

- Install packages via the venv pip:

```powershell
.venv\Scripts\pip.exe install scikit-learn pandas numpy scipy matplotlib
```

3) What matters for automation / codegen
- Keep changes out of `.venv/` — modify only project files (root or subfolders).
- Use `random_state=42` and `np.random.seed(42)` for reproducible runs (this repo relies on that convention).
- Follow existing variable naming: `X_train`, `X_test`, `y_train`, `y_test`.
- Data pipeline pattern used by humans here (use when scaffolding code):
	- Load (pandas.read_csv)
	- Inspect (`.shape`, `.info()`, `.describe()`)
	- Preprocess (StandardScaler / encoders)
	- Split (train_test_split(random_state=42))
	- Train / evaluate (sklearn estimators and metrics)

4) Libraries & integration points
- Primary libs: scikit-learn, pandas, numpy, scipy, matplotlib (already documented in repo).
- No external APIs, no DB connections — treat datasets as local files. When suggesting new dependencies, prefer lightweight, commonly available packages.

5) Project-specific conventions and examples
- Single-file entry: modify or extend `test.py` when adding quick experiments or small modules.
- Prefer `sklearn.pipeline.Pipeline` or explicit `StandardScaler` usage for preprocessing.
- Example pattern for splitting and training (use verbatim style):

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```

6) Safety and repo rules for the agent
- Do not create or modify `.venv/` files.
- Keep edits to project-root `.py` files and new modules under project root.
- If proposing new top-level files, add a one-line comment header explaining purpose.

7) Deliverables for common tasks
- Add a new model training script: create `train_<task>.py`, follow naming and random seed rules, include minimal `if __name__ == '__main__'` runner.
- Add tests (optional): place simple assertion-based script `tests/test_<name>.py` to validate data shapes and reproducibility.

8) Where to look for context
- Entry/script: `test.py`
- Repo root: avoid `.venv/`

9) Questions to ask the maintainer
- Where should persistent datasets live (project root or a data/ directory)?
- Do you want new experiment scripts committed as separate files or as branches/PRs only?

---
If this looks good I will refine any section you want expanded (examples, run experiments, or a small template script). Please tell me if you prefer a `data/` directory or inline CSVs in the root.
