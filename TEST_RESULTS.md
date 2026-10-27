# Test Results - Day 8

Command: `python test_scenarios.py` (runs `python -m expense_tracker.main` with scripted input)
Python: Python 3.12.3  |  Date: 2026-10-27

```
[PASS] 1. python -m expense_tracker.main starts the menu
[PASS] 2. Valid expense stored with confirmation
[PASS] 3. Blank description and invalid amount show help, retry works
[PASS] 4. nan, inf and negative amounts rejected
[PASS] 5. View lists items and total is correct (170.50)
[PASS] 6. Invalid menu choice shows message and menu continues
[PASS] 7. Exit option ends cleanly (code 0, no traceback)
[PASS] 8. Importing modules does not start the menu
[PASS] Extra A. EOFError handled cleanly (no traceback)
[PASS] Extra B. EOFError mid-input handled cleanly
[PASS] Extra C. KeyboardInterrupt handled cleanly (no traceback)

11/11 checks passed
```

## Manual sample run
```

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): Enter description: Enter amount: Added: Tea - 20.00

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): Enter description: Enter amount: Added: Lunch - 150.50

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): 
--- Expenses ---
1. Tea - 20.00
2. Lunch - 150.50

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): Total expenses: 170.50

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): Invalid choice. Please enter 1, 2, 3 or 4.

=== Expense Tracker ===
1. Add expense
2. View expenses
3. Show total
4. Exit
Choose an option (1-4): Goodbye!
```
