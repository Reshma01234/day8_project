# Day 8 - Expense Tracker (Modules & Packages)

**Run command** (from inside `day8_project`, the folder that contains `expense_tracker`):

    python -m expense_tracker.main        # or python3 on some systems

## Structure and responsibilities

    day8_project/
        expense_tracker/
            __init__.py     marks the folder as a package (kept empty)
            main.py         entry point: menu loop, coordination, EOF/Ctrl+C handling, main guard
            expenses.py     add_expense, view_expenses, calculate_total, show_total
            validation.py   parse_amount, get_description, get_amount
        practice_exercises/ Exercises 1-5 (greeting, import styles, isfinite, random, main guard)
        test_scenarios.py   runs the 8 required test scenarios + EOF/Ctrl+C checks
        TEST_RESULTS.md     output of the test run
        DEBUGGING_NOTES.md  problems met and how they were fixed

## Import direction (no circular imports)

    main.py --> expenses.py --> validation.py

validation.py imports only `math`. expenses.py imports validation.py. main.py imports expenses.py.
Nothing imports main.py.

## Behaviour kept from Day 7

- Add / view / total / exit menu
- Blank descriptions rejected with a message, user can retry
- Amounts that are not numbers, are nan / inf / -inf, or are negative are rejected, user can retry
- Invalid menu choice prints a message and the menu continues
- EOFError and KeyboardInterrupt exit cleanly with no traceback
- No classes, files, databases, APIs or pip packages added
