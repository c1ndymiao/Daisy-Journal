from datetime import datetime

def get_entries():
    '''Reads the user's journal entries in my_journal.txt and extracts the logged information.
    Input: None - reads the file strings.
    Output: Returns each line as a list [date, mood, water, sleep, gratitude]'''
    
    entries = []
    journal = "my_journal.txt"

    with open(journal, "r") as infile:
        lines = infile.readlines()
        if len(lines) == 0:
            print("Begin by writing an entry before analyzing your journal.")
            return []
    
        for line in lines:
            line = line.strip()
            sep_log = line.split(", ")

            entry_date = sep_log[0]

            mood_log = sep_log[1].split(": ")
            mood = int(mood_log[1])

            water_log = sep_log[2].split(": ")
            water = float(water_log[1].split(" ")[0])

            sleep_log = sep_log[3].split(": ")
            sleep = float(sleep_log[1].split(" ")[0])

            gratitude = sep_log[4].split(": ")[1]

            entry = [entry_date, mood, water, sleep, gratitude]
            entries.append(entry)

    return entries

def sort_entries(entries, days):
    '''Sorts journal entries into a list of lists for a specified time frame.
    Input: entries list from get_entries() and timeframe (days) from the user's selection.
    Output: A sorted list of entries within the chosen days (last week/month/year)
    
    Example: [ [date, mood, water, sleep, gratitude], [date 2, mood 2, water 2, sleep 2, gratitude 2]]'''

    sorted_e = []
    today = datetime.today()

    for entry in entries:
        entry_date = datetime.strptime(entry[0], "%Y/%m/%d")
        time_diff = (today - entry_date).days

        if time_diff <= days:
            sorted_e.append(entry)
    
    return sorted_e

def entries_avg (entries):
    '''Computes average mood, water intake and hours of sleep the user logged in the chosen timeframe.
    Input: list of entries from sort_entries()
    Output: average mood, average water, average sleep rounded to 2 decimal places.'''
    
    mood_total = 0
    water_total = 0
    sleep_total = 0

    num_days = len(entries)

    if num_days == 0:
        return 0, 0, 0

    for entry in entries:
        mood_total = mood_total + entry[1]
        water_total = water_total + entry[2]
        sleep_total = sleep_total + entry[3]

    avg_mood = mood_total / num_days
    avg_water = water_total / num_days
    avg_sleep = sleep_total / num_days

    return avg_mood, avg_water, avg_sleep

def print_avg(avg_mood, avg_water, avg_sleep):
    '''Prints computed averages.
    Input: avg_mood, avg_water, avg_sleep from entries_avg()
    Output: Prints to terminal.'''

    print("Average mood: ", round(avg_mood, 1))
    print("Average cups of water drank: ", round(avg_water, 1))
    print("Average hours of sleep: ", round(avg_sleep, 2))

def analyze_journal(days):
    '''Analyzes journal entries in the user's selected timeframe and calls on other functions to compute and print averages.
    Input: Chosen timeframe from run_analysis()
    Output: None - calls on print_avg() to print averages to terminal.'''

    entries = get_entries()
    entries_sorted = sort_entries(entries, days)

    if len(entries_sorted) == 0:
        print("No entries to analyze in this past timeframe.")
        return
    
    averages = entries_avg(entries_sorted)
    avg_mood = averages[0]
    avg_water = averages[1]
    avg_sleep = averages[2]
    print_avg(avg_mood, avg_water, avg_sleep)