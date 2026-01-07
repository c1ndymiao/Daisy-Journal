# Daisy
### Instructions

Welcome to Daisy!

This Python program is a wellness journal tracking your daily mood, water intake, sleep hours and gratitude. Daisy also provides you with mindful messages based on your daily entries and calculates your average wellness logs in a timeframe.

Write your first entry and begin your wellness journey!

### Navigation

In the terminal, run the main program with python journal.py.

A main menu will be displayed with 3 options:
1. Write a new entry
2. Analyze your journal
3. Exit

Input the corresponding number to complete an action.

### Write a new entry

Select 1 in the main menu.

You will be prompted to enter the date for the entry in YYYY MM DD format.

Then, you will be prompted to enter your logs:  

**Mood**
```
On a scale of 1 (low) to 5 (high), how did you feel today?
```
Only takes integers.  
Sample Input: 4

**Water**
```
How many cups of water did you drink today?
```
Takes integers and decimals.  
Sample Input: 4.5

**Sleep**
```
How many hours of sleep did you get last night?
```
Takes integers and decimals.  
Sample Input: 7.5

**Gratitude**
```
Something you are grateful for today.
```
Sample Input: "A warm and delicious dinner with my family."

Once logged, your entry will be saved and written into my_journal.txt.

Sample entry:
```
2025/11/19, mood: 4, water: 4.5 cups, sleep: 7.5 hours, grateful for: A warm and delicious dinner with my family.
```
The program additionally outputs mindful messages based on your mood, water and sleep logs. Friendly messages will appear based on how you are feeling and health reminders will appear based on your water intake and hours of sleep.

### Analyze your journal

Select 2 in the main menu.

You will be prompted to choose a timeframe to analyze your entries and compute averages from.
1. Last week (7 days)
2. Last month (30 days)
3. Last year (365 days)

Input 1, 2, or 3.

The program will output your average logs for mood, water and sleep for the chosen timeframe.

### Exit

Select 3 in the main menu.  
Will stop running the program and leave your journal.  
To open Daisy again, run the main program with python journal.py.

Happy journaling!