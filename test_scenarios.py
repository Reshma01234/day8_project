"""Runs the 8 required Day 8 test scenarios against the package.

Run from the day8_project folder:  python test_scenarios.py
"""

import subprocess
import sys

CMD = [sys.executable, "-m", "expense_tracker.main"]
results = []


def run_app(lines):
    """Run the app with the given input lines; return (output, exit code)."""
    proc = subprocess.run(CMD, input="\n".join(lines) + "\n",
                          capture_output=True, text=True, timeout=10)
    return proc.stdout + proc.stderr, proc.returncode


def check(name, condition):
    results.append((name, condition))
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")


# 1. Package imports and menu starts
out, code = run_app(["4"])
check("1. python -m expense_tracker.main starts the menu",
      "=== Expense Tracker ===" in out and code == 0)

# 2. Add a valid expense
out, _ = run_app(["1", "Tea", "20", "4"])
check("2. Valid expense stored with confirmation", "Added: Tea - 20.00" in out)

# 3. Blank description / invalid amount -> message, then retry works
out, _ = run_app(["1", "", "Lunch", "abc", "150", "4"])
check("3. Blank description and invalid amount show help, retry works",
      "Description cannot be blank" in out and "Invalid amount" in out
      and "Added: Lunch - 150.00" in out)

# 4. nan, inf, negative rejected
out, _ = run_app(["1", "Bad", "nan", "inf", "-5", "10", "4"])
check("4. nan, inf and negative amounts rejected",
      out.count("Invalid amount") == 3 and "Added: Bad - 10.00" in out)

# 5. View and total are correct
out, _ = run_app(["1", "Tea", "20", "1", "Lunch", "150.50", "2", "3", "4"])
check("5. View lists items and total is correct (170.50)",
      "1. Tea - 20.00" in out and "2. Lunch - 150.50" in out
      and "Total expenses: 170.50" in out)

# 6. Invalid menu choice -> menu continues
out, _ = run_app(["9", "x", "", "4"])
check("6. Invalid menu choice shows message and menu continues",
      out.count("Invalid choice") == 3 and "Goodbye!" in out)

# 7. Exit cleanly
out, code = run_app(["4"])
check("7. Exit option ends cleanly (code 0, no traceback)",
      "Goodbye!" in out and code == 0 and "Traceback" not in out)

# 8. Importing a module does not start the menu
proc = subprocess.run(
    [sys.executable, "-c",
     "import expense_tracker.main, expense_tracker.expenses, "
     "expense_tracker.validation; print('IMPORT_OK')"],
    capture_output=True, text=True, timeout=10, input="")
check("8. Importing modules does not start the menu",
      "IMPORT_OK" in proc.stdout and "Expense Tracker" not in proc.stdout)

# Extra: EOF and Ctrl+C handling (Day 7 requirement kept)
out, code = run_app([])  # immediate EOF
check("Extra A. EOFError handled cleanly (no traceback)",
      "Traceback" not in out and code == 0)
out, code = run_app(["1", "Tea"])  # EOF in the middle of adding
check("Extra B. EOFError mid-input handled cleanly",
      "Traceback" not in out and code == 0)
proc = subprocess.run(
    [sys.executable, "-c",
     "import builtins\n"
     "def boom(*a, **k): raise KeyboardInterrupt\n"
     "builtins.input = boom\n"
     "from expense_tracker.main import main\n"
     "main()"],
    capture_output=True, text=True, timeout=10)
check("Extra C. KeyboardInterrupt handled cleanly (no traceback)",
      "Traceback" not in proc.stderr and proc.returncode == 0)

passed = sum(ok for _, ok in results)
print(f"\n{passed}/{len(results)} checks passed")
sys.exit(0 if passed == len(results) else 1)
