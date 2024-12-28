from time import sleep
import cli_utils as cu
import datetime as dt
import notification_utils as nu

current_year = dt.now().year
present_day = dt.today()
yesterday = present_day - dt.timedelta(1)
tomorrow = present_day + dt.timedelta(1)

def get_dates():
    cal = cu.Calendar()
    cal.load_events()
    ndates = []
    for event in cal.events:
        ndates.append(event.notification)
    len_ndates = len(ndates)
    for i in range(len_ndates):
        ndates[i] = dt.strptime(ndates[i], "%Y-%m-%d:%H:%M")
    return ndates


def watch():
    ndates = get_dates()
    while True:
        if present_day in ndates:
            nu.display_notification()
        sleep(60)