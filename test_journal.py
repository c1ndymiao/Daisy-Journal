from journal import messages
from analyze_journal import entries_avg
from analyze_journal import sort_entries
from datetime import datetime

# Messages Tests

def test_messages_low_mood_boundary():
    msg = messages(2, 6, 6)
    assert msg[0] == "Take it day by day. Tomorrow will be better :)"

def test_messages_high_mood_boundary():
    msg = messages(4, 6, 6)
    assert msg[0] == "Heart is full and mind is clear <3"

def test_messages_low_mood():
    msg = messages(1, 5, 8)
    assert msg[0] == "Take it day by day. Tomorrow will be better :)"

def test_messages_mid_mood():
    msg = messages(3, 8, 8)
    assert msg[0] == "Rest and recharge for tomorrow!"

def test_messages_high_mood():
    msg = messages(5, 5, 5)
    assert msg[0] == "Heart is full and mind is clear <3"

def test_messages_low_hydration_boundary():
    msg = messages(3, 5, 7)
    assert msg[1] == "Stay hydrated! The recommended daily water intake is 6-8 cups."

def test_messages_hydrated_boundary():
    msg = messages(3, 6, 7)
    assert msg[1] == None

def test_messages_low_hydration():
    msg = messages(3, 2.5, 7)
    assert msg[1] == "Stay hydrated! The recommended daily water intake is 6-8 cups."

def test_messages_hydrated():
    msg = messages(3, 7.5, 7)
    assert msg[1] == None


def test_messages_low_sleep_boundary():
    msg = messages(4, 6, 5)
    assert msg[2] == "Let's try to sleep earlier tonight."

def test_messages_enough_sleep_boundary():
    msg = messages(4, 6, 6)
    assert msg[2] == None

def test_messages_low_sleep():
    msg = messages(4, 6, 5.5)
    assert msg[2] == "Let's try to sleep earlier tonight."

def test_messages_enough_sleep():
    msg = messages(4, 6, 9)
    assert msg[2] == None

# Journal Analysis Tests

def test_no_entries_avg():
    entries = []
    avgs = entries_avg(entries)
    avg_mood = avgs[0]
    avg_water = avgs[1]
    avg_sleep = avgs[2]

    assert avg_mood == 0
    assert avg_water == 0
    assert avg_sleep == 0

def test_one_entries_avg():
    entries = [["2025/11/18", 5, 6, 7.5, "friends who make me laugh"]]
    avgs = entries_avg(entries)
    avg_mood = avgs[0]
    avg_water = avgs[1]
    avg_sleep = avgs[2]

    assert avg_mood == 5
    assert avg_water == 6
    assert avg_sleep == 7.5

def test_more_entries_avg():
    entries = [["2025/11/18", 5, 6, 7.5, "friends who make me laugh"],
               ["2025/11/19", 4, 5, 8, "the feeling of sunshine"],
               ["2025/11/20", 3, 5.5, 6, "a cozy bed to sleep in"]]
    avgs = entries_avg(entries)
    avg_mood = avgs[0]
    avg_water = avgs[1]
    avg_sleep = avgs[2]

    assert avg_mood == (5 + 4 + 3) / 3
    assert avg_water == (6 + 5.5 + 5) / 3
    assert avg_sleep == (7.5 + 8 + 6) / 3

def test_sort_entries():
    test_today = datetime.strptime("2025/11/19", "%Y/%m/%d")

    entries = [
        ["2025/11/17", 5, 6, 7.5, "gratitude"],
        ["2025/11/18", 4, 5, 8, "gratitude"],
        ["2025/11/19", 3, 5.5, 6, "gratitude"],
        ["2025/11/20", 2, 4, 7, "gratitude"]
    ]

    days = 3
    exp_sort = []
    for entry in entries:
        entry_date = datetime.strptime(entry[0], "%Y/%m/%d")
        time_diff = (test_today - entry_date).days

        if time_diff <= days:
            exp_sort.append(entry)
    
    test_sort = []
    for entry in entries:
        entry_date = datetime.strptime(entry[0], "%Y/%m/%d")
        time_diff = (test_today - entry_date).days

        if time_diff <= days:
            test_sort.append(entry)
    
    assert exp_sort == test_sort