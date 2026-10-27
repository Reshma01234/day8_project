# Debugging Notes - Day 8

## 1. ModuleNotFoundError when running main.py directly
- **Command:** `python expense_tracker/main.py`
- **Error:** `ModuleNotFoundError: No module named 'expense_tracker'`
- **Cause:** Running a file as a script puts the *file's own folder* on the import path, not the
  project folder, so `from expense_tracker.expenses import ...` cannot find the package.
- **Fix:** Run it as a module from `day8_project`: `python -m expense_tracker.main`.

## 2. ModuleNotFoundError when running from the wrong folder
- **Command:** `cd expense_tracker` then `python -m expense_tracker.main`
- **Error:** `No module named 'expense_tracker'`
- **Cause:** `-m` looks for the package starting from the current folder. Inside `expense_tracker/`
  there is no `expense_tracker` folder to find.
- **Fix:** `cd` back to `day8_project` (the folder that contains `expense_tracker`) first.

## 3. nan and inf passed `float()` conversion
- `float("nan")` and `float("inf")` do not raise ValueError, so try/except alone is not enough.
- **Fix:** After converting, check `math.isfinite(value)`, then reject negatives.

## 4. Menu must not start on import
- Startup code is behind `if __name__ == "__main__": main()` so importing a module only loads
  the functions. Verified by test 8.

## Rules to remember
- Never name your own files `math.py`, `random.py`, `json.py` etc. (they can hide the real module).
- Prefer explicit imports; avoid `from module import *`.
