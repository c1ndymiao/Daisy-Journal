# How to Test

To test the logic of the Daisy program, there are two ways to verify the project works as expected.

1. Automated pytests
2. Manual tests

### Automated Pytests

To run all tests at once, run the following command in the terminal:
pytest --verbose test_journal.py

This will run all the pytests in the test_journal.py file and verify the assertions as pass/fail. There are three categories of automated tests found in test_journal.py. The following are descriptions of the minimal tests to ensure Daisy runs as expected.

**1. messages() pytests**

Verifies that the program generates and stores the appropriate wellness messages based on the user's input of entry data for mood, water intakes and hours of sleep.

***Mood Boundary Tests***

test_messages_low_mood_boundary()
* mood = 2
* expected message: "Take it day by day. Tomorrow will be better :)"

test_messages_high_mood_boundary()
* mood = 4
* expected message: ""Heart is full and mind is clear <3"

test_messages_mid_mood()
* mood = 3
* expected message: "Rest and recharge for tomorrow!"

***Water Intake Boundary Tests***

test_messages_low_hydration_boundary()
* water_intake = 5  
* expected message: "Stay hydrated! The recommended daily water intake is 6-8 cups."

test_messages_hydrated_boundary()
* water_intake = 6
* expected message: No message, value stored in list should be None

***Sleep Boundary Tests***

test_messages_low_sleep_boundary()
* sleep_hours = 5
* expected message: "Let's try to sleep earlier tonight."

test_messages_enough_sleep_boundary()
* sleep_hours = 6
* expected message: No message, value stored in list should be None

**2. entries_avg() tests**

Verifies that the program computes the correct average for mood, water intake and hours of sleep based on a list of logs.

test_no_entries_avg()
* entries: empty list []
* expected average: 0

test_one_entries_avg()

* entries: one entry

e.g. ["2025/11/18", 5, 6, 7.5, "friends who make me laugh"]

* expected average: each average for sleep, water and hours of sleep should be equal to the single entry's log  
*respectively to the example above:*  
avg_mood == 5  
avg_water == 6  
avg_sleep == 7.5

test_more_entries_avg()
* entries: a list of list with multiple entries
* expected average: extracts values for logs of mood, water intake and hours of sleep and divides the sum for each log category over the number of entries

**3. sort_entries() tests**

Verifies that the entries for a specific timeframe (number of days) are stored correctly.

test_sort_entries()
* compares each entry to a reference date (today) and only entries with a time difference up to the reference date are added to a list

### Manual Tests

To manually test that Daisy works as expected when a user interacts with the journal, try the following actions.

**1. Navigation**

Objective: Be able to navigate from the main menu to complete different actions.

Program will display: 
```
⊱ ──────── {.⋅ ✯ ⋅.} ──────── ⊰
Welcome to Daisy: Your daily journal!
Main Menu  
ʚ⁺˖↪ 1. Write a new entry
ʚ⁺˖↪ 2. Analyze your journal 
ʚ⁺˖↪ 3. Exit
```
Input: 1  
Expected Output: Program will run date_entry() and prompt user to enter the entry date starting with "Year (YYYY): "

Input: 2  
Expected Output: Program will display another menu
```
Analyzing your journal...  
Select a timeframe to analyze:  
1. Last week  
2. Last month  
3. Last year
```
Input: 3  
Expected Output: Program will print "Goodbye, see you tommorow!" and user will no longer be in the Daisy program.

No matter where you navigate, when you are done with that action, the program should take you back to the main menu until you input 3 to exit.

**2. Writing a new entry**

Objective: Be able to log a journal entry that will be written into my_journal.txt

From the main menu, enter 1, then follow the instructions to logging a entry.

a) date: YYYY MM DD - e.g 2025 11 20  
b) On a scale of 1 (low) to 5 (high), today I felt: - e.g 5  
c) I drank _ cups of water today: - e.g 3.5  
d) I got _ hours of sleep last night: - e.g 7  
e) Today, I am grateful for: - e.g Family and friends.

Once finished with inputs, the program should print: "Daily log successfully saved."

The entry should be written into my_journal.txt in the following format:  
*respectively to the example above:*   

"2025/11/20, mood: 5, water: 3.5 cups, sleep: 7.0 hours, grateful for: Family and friends."



**3. Recieving wellness messages**

Objective: Based on your entry logs, the program will output different messages.

For mood logs less than or equal to 2, the program will print:  
```
Take it day by day. Tomorrow will be better :)
```
For mood logs equal to 3, the program will print:  
```
Rest and recharge for tomorrow!
```
For mood logs greater than or equal to 4, the program will print:  
```
Heart is full and mind is clear <3
```
For water logs less than 6, the program will print:  
```
Stay hydrated! The recommended daily water intake is 6-8 cups.
```
For water logs greater than or equal to 6, no message will be printed for hydration.

For sleep logs less than 6, the program will print:  
```
Let's try to sleep earlier tonight.
```
For sleep logs greater than 6, no message will be printed for sleep.


Using the sample input from Writing a new entry, the program should output:
```
────────˚₊‧꒰ა ✉︎ ໒꒱ ‧₊˚───────
Your daily wellness messages:
Heart is full and mind is clear <3 
Stay hydrated! The recommended daily water intake is 6-8 cups.
```
**4. Running journal analysis**

Objective: Check that the program calculates the correct average.

Once you write atleast 1 entry, you will be able to compute averages for mood, water intake and hours of sleep.
If there are no entries, should averages will be computed as 0.

Select a timeframe option from the menu, either 1, 2, or 3.

Expected output:
```
Average mood: [average]
Average cups of water drank:  [average]
Average hours of sleep: [average]
```