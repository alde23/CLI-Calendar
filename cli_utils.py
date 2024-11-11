import json
from datetime import date as dt
from datetime import time as tm
from datetime import datetime as dtm
from datetime import timedelta
from calendar import TextCalendar

txt_cal = TextCalendar()

current_year = dtm.now().year

present_day = dtm.today()
yesterday = present_day - timedelta(1)
tomorrow = present_day + timedelta(1)


class Event:

    def __init__(self, title, date, description, time, notification):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.notification = notification

class Calendar:

    def __init__(self):
        self.events = []
        self.finished = []
        self.events_is_loaded = False
        self.finished_is_loaded = False

    def load_events(self):
        file_name = "data/events.json"
        type_name = "events"

        with open(file_name, 'r') as sf:
            data = json.load(sf)
            for event in data.get(type_name, []):
                event_tba = Event(
                    title = event["title"],
                    description = event["description"],
                    date = dt.fromisoformat(event["date"]),
                    time = tm.fromisoformat(event["time"]),
                    notification = event["notification"]
                )

                self.events.append(event_tba)

            if len(self.events):
                self.events_is_loaded = True


    def load_finished(self):
        file_name = "data/finished.json"
        type_name = "finished"

        with open(file_name, 'r') as sf:
            data = json.load(sf)
            for event in data.get(type_name, []):
                event_tba = Event(
                    title = event["title"],
                    description = event["description"],
                    date = dt.fromisoformat(event["date"]),
                    time = tm.fromisoformat(event["time"]),
                    notification = event["notification"]
                )

                self.finished.append(event_tba)

            if len(self.finished):
                self.finished_is_loaded = True


    def print_events(self):
        print("Loaded Events:")
        for event in self.events:
            print(
                f"Title: {event.title}, Date: {event.date}, Time: {event.time}, Description: {event.description}, Notification: {event.notification}")

        print("\nFinished Events:")
        for event in self.finished:
            print(
                f"Title: {event.title}, Date: {event.date}, Time: {event.time}, Description: {event.description}, Notification: {event.notification}")


    def already_exists(self, date, title):
        for event in self.events:
            if event.date == date and event.title == title:
                print("Event title must be unique!!")
                return True


    def add_event(self, args):
        if not self.events_is_loaded:
            exit(1)
        if self.already_exists(args.date, args.title):
            exit(1)
        if args.description is None:
            args.description = "No description..."
        if args.time is None:
            args.time = tm.fromisoformat("09:00")

        new_event = Event(
            title = args.title,
            description = args.description,
            date = args.date,
            time = args.time,
            notification = args.notification
        )

        self.events.append(new_event)


    def finish_event(self, args):
        if not self.finished_is_loaded:
            exit(1)
        for event in self.events:
            if event.title == args.title and event.date == args.date:
                self.finished.append(event)
                self.events.remove(event)

    def delete_event(self, args):
        if not self.finished_is_loaded:
            exit(1)
        for event in self.events:
            if event.title == args.title and event.date == args.date:
                self.events.remove(event)


    def modify_event(self, args):
        if not self.events_is_loaded:
            exit(1)
        for event in self.events:
            if event.title == args.title and event.date == args.date:
                if args.description:
                    event.description = args.description
                if args.time:
                    event.time = args.time
                if args.notification:
                    event.notification = args.notification
                if args.modify:
                    event.title = args.modify
                if args.set:
                    event.date = args.set
                break


    @staticmethod
    def show_calendar(args):
        if args.year and args.month:
            txt_cal.prmonth(int(args.year), int(args.month))
        elif args.year:
            txt_cal.pryear(int(args.year))
        elif args.month:
            txt_cal.prmonth(current_year, int(args.month))
        else:
            txt_cal.pryear(current_year)


    def list_events(self, args):
        current_events = []
        if args.date is None:
            args.date = present_day
        else:
            args.date = dt.fromisoformat(args.date)

        for event in self.events:
            if event.date == args.date:
                current_events.append(event)

        date_str = args.date.strftime("%Y-%m-%d")
        print(f"Events for the date {date_str}")
        print("")
        for event_l in current_events:
            time_str = event_l.time.strftime("%H:%M")
            print(f"{time_str} {event_l.title} ")


    def date_to_str(self):
        for event in self.events:
            event.date = event.date.strftime('%Y-%m-%d')
            event.time = event.time.strftime('%H:%M')

        for event_f in self.finished:
            event_f.date = event_f.date.isoformat()
            event_f.time = event_f.time.isoformat()

    def update_db(self):
        self.date_to_str()
        data = {"events": [event.__dict__ for event in self.events]}
        with open("data/events.json", "w") as f:
            json.dump(data, f, indent=4)
        data_f = {"finished": [finished.__dict__ for finished in self.finished]}
        with open("data/finished.json", "w") as f:
            json.dump(data_f, f, indent=4)