import calendar
import json


# Prints the inputted month as a text calendar
def show_m(year, month):
    print("")
    calendar.prmonth(year, month)


# Prints the inputted year as a text calendar
def show_y(year):
    text_calendar = calendar.TextCalendar()
    print("")
    text_calendar.pryear(year)


# Appends json file with new task
def add_event(event, filename="data/events.json"):
    try:
        # Load existing tasks from the JSON file
        with open(filename, "r") as f:
            data = json.load(f)
            # Check if "events" key exists and is a list
            if "events" not in data or not isinstance(data["events"], list):
                data["events"] = []
    except FileNotFoundError:
        # If file does not exist, create the structure with an empty "events" list
        data = {"events": []}

    # Append the new task to the "events" list
    data["events"].append(event)

    # Write the updated data back to the file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def event_exists(event_f, source_file="data/events.json"):
    # Check if task is in data/events.json
    try:
        with open(source_file, "r") as sf:
            data = json.load(sf)
            events = data.get("events", [])

            for event in events:
                if all(event.get(key) == value for key, value in event_f.items()):
                    return True

            return False

    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
        return False

def get_event_by_name_date(event_f, filename="data/events.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            events = data.get("events", [])


def finish_event(event_f, source_file="data/events.json", destination_file="data/finished.json"):
    if event_exists(event_f, source_file):
        with open(source_file, "r") as sf:
            data = json.load(sf)
            events = data.get("events", [])

        # Get matching event(s)
        events = [event for event in events if all(event.get(key) == value for key, value in event_f.items())]

        add_event(event_f, destination_file)


