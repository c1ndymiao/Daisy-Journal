from analyze_journal import analyze_journal

def entry_data():
    ''' Takes input from the user for their daily journal entry. 
    Input: mood (1-5), water intake (# of cups), hours of sleep, statement of gratitude
    Output: returns a list [mood, water_intake, sleep_hours, gratitude]'''

    mood_min = 1
    mood_max = 5
    water_min = 0
    sleep_min = 0

    mood = int(input("On a scale of 1 (low) to 5 (high), today I felt: "))
    while mood < mood_min or mood > mood_max:
        mood = int(input("Error: Mood log must be between 1-5." + '\n' + "On a scale of 1 (low) to 5 (high), today I felt: "))
    
    water_intake = float(input("I drank _ cups of water today: "))
    while water_intake < water_min:
        water_intake = float(input("Error: Water log must be zero or greater" + '\n' + "I drank _ cups of water today: "))

    sleep_hours = float(input("I got _ hours of sleep last night: "))
    while sleep_hours < sleep_min:
        sleep_hours = float(input("Error: Sleep log must be zero or greater" + '\n' + "I got _ hours of sleep last night: "))

    gratitude = input("Today, I am grateful for: ")
    while gratitude == '':
        gratitude = input("Error: Daily gratitude missing." + '\n' + "Today, I am grateful for: ")

    entry = [mood, sleep_hours, water_intake, gratitude]
    return entry

def write_entry(date, entry):
    ''' Formats and writes a daily journal entry into "my_journal.txt" onto a new line.
    Input: date (YYYY/MM/DD), entry list from entry_data() [mood, sleep_hours, water_intake, gratitude]
    Output: Writes to my_journal.txt file'''

    mood = entry[0]
    sleep_hours = entry[1]
    water = entry[2]
    gratitude = entry[3]

    journal = "my_journal.txt"
    with open(journal, 'a') as outfile:
        outfile.write(f"{date}, mood: {mood}, water: {water} cups, sleep: {sleep_hours} hours, grateful for: {gratitude}" + '\n')

def messages(mood, water_intake, sleep_hours):
    '''Generates wellness messages based on the user's daily logged mood, water intake and hours of sleep.
    Input: from entry_data() - mood (1-5), water intake (# of cups), hours of sleep
    Output: Appropriate messages are appended to a list as strings.'''

    water_thres = 6
    sleep_thres = 6

    msgs = []
    if mood <= 2:
        msgs.append("Take it day by day. Tomorrow will be better :)")
    elif mood == 3:
        msgs.append("Rest and recharge for tomorrow!")
    elif mood >= 4:
        msgs.append("Heart is full and mind is clear <3")
    
    if water_intake < water_thres:
        msgs.append("Stay hydrated! The recommended daily water intake is 6-8 cups.")
    else:
        msgs.append(None)
    if sleep_hours < sleep_thres:
        msgs.append("Let's try to sleep earlier tonight.")
    else:
        msgs.append(None)
    
    return msgs

def print_messages(mood, water_intake, sleep_hours):
    '''Prints the wellness messages generated and stored in the list from messages().
    Input: from entry_data() - mood (1-5), water intake (# of cups), hours of sleep
    Output: Prints messages in terminal.'''
    
    for msg in messages(mood, water_intake, sleep_hours):
        if msg != None:
            print(msg)

def date_entry():
    '''Prompts the user to enter the date for their entry in YYYY MM DD and formats it.
    Input: year, month and day entered by user
    Output: YYYY/MM/DD string'''
    
    year_min = 1000
    year_max = 3000

    year = int(input("Year (YYYY): "))
    while year < year_min or year > year_max:
        year = int(input("Error. Enter a valid year (YYYY): "))

    month = int(input("Month (MM): "))
    while month < 1 or month > 12:
        month = int(input("Error. Enter a valid month (MM): "))

    day = int(input("Day (DD): "))
    while day < 1 or day > 31:
        day = int(input("Error. Enter a valid day (DD): "))

    date = f"{year}/{month}/{day}"
    return date

def run_analysis():
    ''' Prompts the user for a timeframe to analyze their entries.
    Input: 1, 2, 3 entered by the user
    Output: Calls analyze_journal() to compute averages for that timeframe.'''

    time = int(input("Enter 1, 2 or 3: "))
    while time < 1 or time > 3:
            time = int(input("Error. Select a valid timeframe: "))
    
    week = 7
    month = 30
    year = 365

    if time == 1:
        analyze_journal(week)
    elif time == 2:
        analyze_journal(month)
    elif time == 3:
        analyze_journal(year)
        

def main():
    '''Runs the Daisy Python program menu and user interface. Calls on logic functions based on user selection. 
    Input: Based on user navigation.
    Output: User interface and Daisy features such as writing an entry and the user's journal analysis.'''
    
    running = True
    while running:
        print("⊱ ──────── {.⋅ ✯ ⋅.} ──────── ⊰")
        print("Welcome to Daisy: Your daily journal!")
        print("Main Menu")
        print("ʚ⁺˖↪ 1. Write a new entry")
        print("ʚ⁺˖↪ 2. Analyze your journal" )
        print("ʚ⁺˖↪ 3. Exit")
        
        nav = int(input("What do you want to do? Enter 1, 2 or 3: "))

        while nav < 1 or nav > 3:
            nav = int(input("Error. What do you want to do? Enter 1, 2 or 3: "))
    
        if nav == 1:
            date = date_entry()
            entry = entry_data()
            write_entry(date, entry)
            print("Daily log successfully saved." + '\n')

            print("────────˚₊‧꒰ა ✉︎ ໒꒱ ‧₊˚───────")
            print("Your daily wellness messages:")
            print_messages(entry[0], entry [1], entry [2])
        elif nav == 2:
            print("Analyzing your journal...")
            print("Select a timeframe to analyze:")
            print("1. Last week")
            print("2. Last month")
            print("3. Last year")
            run_analysis()
        elif nav == 3:
            print("Goodbye, see you tommorow!")
            running = False

if __name__ == "__main__":
    main()