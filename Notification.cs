using System;
using System.Collections.Generic;

public static class Notification
{
    private const string OngoingEventsFile = "ongoingEvents.json";

    public static void ShowTodayEvents()
    {
        var events = EventStorage.LoadEvents(OngoingEventsFile);
        var todayEvents = events.FindAll(e => e.Date.Date == DateTime.Now.Date);

        if (todayEvents.Count > 0)
        {
            Console.WriteLine("Events for today:");
            foreach (var e in todayEvents)
            {
                Console.WriteLine($"- {e.Title}: {e.Description}");
            }
        }
        else
        {
            Console.WriteLine("No events for today.");
        }
    }
}
