# Day 8 – Expense Tracker (Modules & Packages)

AhamVerse Technologies – Python Intern Learning Roadmap, Day 8.
The Day 7 Expense Tracker, refactored into a small Python package with separate modules for the menu, expense operations and input validation.

## How to run

From inside `day8_project` (the folder that contains `expense_tracker`):

```
python -m expense_tracker.main
```

On systems that use `python3`:

```
python3 -m expense_tracker.main
```

Requires Python 3 only. No pip packages are needed.

## Project structure

```
day8_project/
├── expense_tracker/
│   ├── __init__.py        # marks the folder as a package (empty)
│   ├── main.py            # entry point, menu loop, EOF/Ctrl+C handling, main guard
│   ├── expenses.py        # add, view, calculate and show total
│   └── validation.py      # get and validate descriptions and amounts
├── practice_exercises/    # Exercises 1-5
├── test_scenarios.py      # runs the required tests
├── NOTES.md
├── DEBUGGING_NOTES.md
├── TEST_RESULTS.md
└── README.md
```

## Modules

| File | Responsibility |
|---|---|
| `main.py` | Menu loop and coordination. Handles `EOFError` and `KeyboardInterrupt`. Contains the `if __name__ == "__main__":` guard. |
| `expenses.py` | `add_expense`, `view_expenses`, `calculate_total`, `show_total` |
| `validation.py` | `parse_amount`, `get_description`, `get_amount` |

Imports go one way: `main.py` → `expenses.py` → `validation.py`. There are no circular imports.

## Features

1. Add expense (description and amount)
2. View expenses
3. Show total
4. Exit

Input handling: blank descriptions, non-numeric amounts, `nan`, `inf` and negative amounts are rejected with a message, and the user can retry. An invalid menu choice shows a message and the menu continues.

## Practice exercises

| Exercise | File(s) | What it shows |
|---|---|---|
| 1. Create a module | `greeting.py`, `app.py` | Import and call a function from another file |
| 2. Import styles | `import_styles.py` | `import math`, `from math import pi`, `import random as rng` |
| 3. Finite number | `finite_check.py` | `math.isfinite()` rejects nan/inf; invalid text handled |
| 4. Random number | `random_demo.py` | `random.randint(1, 10)`; result changes between runs |
| 5. Import safety | `guard_demo.py`, `import_guard_demo.py` | The main guard stops startup code running on import |

Run any of them from inside `practice_exercises/`, for example `python app.py`.

## Testing

```
python test_scenarios.py
```

This runs the 8 required scenarios (start, valid expense, blank/invalid input, nan/inf/negative, view and total, invalid menu choice, exit, import without starting the app) plus EOF and Ctrl+C checks. Results are in `TEST_RESULTS.md`.

## Author

Reshma – [github.com/Reshma01234](https://github.com/Reshma01234)
