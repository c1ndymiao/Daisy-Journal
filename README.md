# Daisy
### Introduction

Daisy is a daily wellness journal designed to help users track and reflect on their wellbeing. It allows users to write daily entries to log their mood, water intake, hours of sleep and a gratitude statement. By spending a few minutes for self-reflection, users are encouraged to gain clarity on their thoughts and identity patters in their lifestyle habits. Daisy aims to help users implement healther routines such as consistent sleep schedules and adequate hydration.

This project was inspired from my own journaling habits. During the pandemic, when days felt slow yet, months passed by quickly, documenting my thoughts and feelings helped me stay grounded. Reflecting and practising gratitude every night before bed taught me to appreciate the small moments and see the bigger picture. I could see my growth as a person, starting my days with intention and setting a positive outlook.

With Daisy, I wished to recreate that experience in a digital program.

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