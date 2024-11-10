import json
from datetime import date as dt
from datetime import time as tm


class Event:

    def __init__(self, title, date, description="...", time="09:00", notification="08:00"):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.notification = notification

class Calendar:

    def __init__(self):
        self.events = []
        self.events_is_loaded = False
        self.finished = []
        self.finished_is_loaded = False

    def load_events_from_file(self, events_type="events"):
        try:
            if events_type == "events":
                file_name = "data/events.json"
                target_list = self.events
                is_loaded_flag = "events_is_loaded"
            elif events_type == "finished":
                file_name = "data/finished.json"
                target_list = self.finished
                is_loaded_flag = "finished_is_loaded"
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            print(f"The {events_type} file was not found.")
            exit(1)

        try:
            with open (file_name, "r") as sf:
                event_data = json.load(sf)

                for event_f in event_data.get(events_type, []):
                    event_l = Event(
                        title = event_f["title"],
                        description = event_f["description"],
                        date = dt.fromisoformat(event_f["date"]),
                        time = tm.fromisoformat(event_f["time"]),
                        notification = event_f["notification"]
                    )

                    target_list.append(event_l)

                if target_list:
                    setattr(self, is_loaded_flag, True)
        except FileNotFoundError:
            print(f"The {events_type} file was not found.")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")


def add_new_event(self, event_a):
    if not self.events_is_loaded:
        exit(1)
    elif not isinstance(event_a, Event):
        exit(1)

    self.events.append(event_a)


def finish_event(self, event_f, to_delete=False):
    if not self.events_is_loaded:
        exit(1)
    elif not self.finished_is_loaded:
        exit(1)
    elif not isinstance(event_f, Event):
        exit(1)

    for event in self.events:
        if event.title == event_f.title and event.date == event_f.date and event.time == event_f.time:
            if not to_delete:
                self.finished.append(event)
            self.events.remove(event)
            return


def list_events(date_l, which_list):

    events_of_the_day = []
    for event in which_list:
        if event.date is date_l:
            events_of_the_day.append(event)
        if len(events_of_the_day) < 1:
            exit(1)
    events_of_the_day.sort(key=events_of_the_day[0].time)

    print(f"Events for the date {date_l}")

    for event in events_of_the_day:
        print(f"{event.time} {event.title}")
















