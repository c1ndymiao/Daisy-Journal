# Test Coverage

### Pytests

To run all tests at once, run the following command in the terminal:
pytest --verbose test_journal.py. This contains 17 pytests.

In the file, I tested the boundaries for messages() and additional possible values for the logs.

For mood, all possible log values between 1 - 5 were covered to have the correct message appended to the output list.

For water intake (hydration), in between log values other than the boundary of 6 were tested to have either the hydration reminder appended or None appended, depending on the user input.

For hours of sleep, in between log values other than the boundary of 6 were tested to have either the sleep reminder appended of None appended, depending on the user input.

### Manual Tests

In addition to testing that the user interface was working properly from how_to_test.md, you may test when the user inputs something out of range.

When writing an entry and logging mood, water intake, hours of sleep and gratitude:

**This specifically tests entry_data():**

Try entering a number less than 1 or greater 5 for the mood input. The program should print to the terminal an error message and continue prompt you to enter a valid mood log until done so.
```
Error: Mood log must be between 1-5.
On a scale of 1 (low) to 5 (high), today I felt:
```
Try entering a number less than 0 for the water input. The program should print to the terminal an error message and continue prompt you to enter a valid water log until done so.
```
Error: Water log must be zero or greater
I drank _ cups of water today: 
```
Try entering a number less than 0 for the sleep input. The program should print to the terminal an error message and continue prompt you to enter a valid sleep log until done so.
```
Error: Sleep log must be zero or greater
I got _ hours of sleep last night: 
```
Try entering skipping the gratitude input. The program should print to the terminal an error message and continue prompt you to enter a valid statement of gratitude until done so.
```
Error: Daily gratitude missing.
Today, I am grateful for:
```

**This specifically tests write_entry():**

Any combination of valid logs will be written into my_journal.txt

**This specifically tests date_entry():**

Try entering a year (YYYY) less than 1000 or greater than 3000. The program should print to the terminal an error message and continue prompt you to enter a valid year until done so.
```
Error. Enter a valid year (YYYY):
```
Try entering a month (MM) less than 1 or greater than 12. The program should print to the terminal an error message and continue prompt you to enter a valid month until done so.
```
Error. Enter a valid month (MM):
```
Try entering a day (DD) less than 1 or greater than 31. The program should print to the terminal an error message and continue prompt you to enter a valid day until done so.
```
Error. Enter a valid day (DD): 
```
**This specifically tests run_analysis():**

When prompted to choose a timeframe to analyze, try choosing  a non-existent option either less than 1 or greater than 3. The program should print to the terminal an error message and continue prompt you to enter a valid choice until done so.
```
Error. Select a valid timeframe: 
```
**This specifically tests the main menu loop in main()**

When prompted for a navigation choise, try choosing a non-existent option either less than 1 or greater than 3. The program should print to the terminal an error message and continue prompt you to enter a valid navigation until done so.
```
Error. What do you want to do? Enter 1, 2 or 3:
```
**This specifically tests get_entries()**

If you have not written any journal entries, the program should output to the terminal:
```
Begin by writing an entry before analyzing your journal.
```
**This specifically tests analyze_journal()**

If you have not written any journal entries, the program should output to the terminal:
```
No entries to analyze in this past timeframe.
```