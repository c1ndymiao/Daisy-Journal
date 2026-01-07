
### Design

When designing Daisy's software, I started with structuring the program around the two core features:
1. Writing an entry
2. Analyzing journal entries

To organize this better, I divided the program into two Python files. This made it easier to understand the flow of my program and write pytests that excluded input prompts and print statements.
1. journal.py handles user interactions, menu navigation and writing entries.
2. analyze_journal.py handles the logic to reading entries and computing averages.

When writing the program, I wrote functions in order of how a typical user would use their Daisy journal. This controlled a structured flow for creating functions that referenced each other.

The first action that takes user input and will trigger other connected subroutines is:
```
nav = int(input("What do you want to do? Enter 1, 2, or 3: "))
```
Then, main() calls the appropriate logic functions.

**When the user inputs 1, for write a new entry, main() will call:**
* date_entry() to validate and format the date
* entry_data() to collect and store mood, water intake, hours of sleep and gratitude
* write_entry() to write the entry into my_journal.txt
* print_messages() to generate the appropriate wellness messages

Through storing the entry data in a list: [mood, water_intake, sleep_hours, gratitude], this structure is reused again in the analysis functions.

I seperated messages() and print_messages() to be able to write automated pytests to test the logic of which messages would appear based on the user's logs.  messages() returns the appropriate messages in a list while print_messages() loops through the list and only print the messages with a non-None value. This kept my main function clean as main() only calls print_messages().

**When the user inputs 2, for analyze your jounal, main() will call:**
* run_analysis which calls analyze_journal(days)

Daisy's logic for the analysis feature is written in analyze_journal.py. This Python file has functions for reading, sorting and calculating the log averages from the user's my_journal.txt.

1. get_entries() seperates the each entry string in my_journal.txt using the split method.
```
sep_log = line.split(", ")
entry_date = sep_log[0]

mood_log = sep_log[1].split(": ")
mood = int(mood_log[1])
```
It extracts only the needed input (values of mood, cups of water, hours of sleep, gratitude) to then return them back into an organized list:
[entry_date, mood, water, sleep, gratitude]

Essentially, it reverses the writing back into the form that entry_data() had.

2. entries_sorted = sort_entries(entries, days) sorts the entries into order by timeframe.

Here, the datetime module is used to reference the current date, convert the entry_dates into calendar days and calculates how many days ago each entry was written. Only entries within the selected timeframe that the user specified to analyze (last 7, 30 or 365 days) are kept.
```
time_diff = (today - entry_date).days
```
3. entries_avg(entries_sorted) computes the averages with loops and mathematical operators.
```
for entry in entries:
    mood_total = mood_total + entry[1]
    water_total = water_total + entry[2]
    sleep_total = sleep_total + entry[3]

avg_mood = mood_total / num_days
avg_water = water_total / num_days
avg_sleep = sleep_total / num_days
```
The logic works with a list so that I was able to write an automated pytest for it to test with a manually created list of entries.

4. print_avg(avg_mood, avg_water, avg_sleep) prints the analyzed averages to the terminal for the user to see.

The main menu is repeated with a while loop so that the user will always be directed back to the main menu until they choose to exit. This makes it easier to use Daisy if they wish to write multiple entries and analyze different timeframes without needing to reopen the program each time.