using System;
using System.Collections.Generic;

public static class EventManager
{
    private const string OngoingEventsFile = "ongoingEvents.json";

    public static void AddEvent(string title, DateTime date, string description)
    {
        var events = EventStorage.LoadEvents(OngoingEventsFile);
        events.Add(new Event { Title = title, Date = date, Description = description });
        EventStorage.SaveEvents(OngoingEventsFile, events);
    }

    public static void ModifyEvent(string title, DateTime newDate, string newDescription)
    {
        var events = EventStorage.LoadEvents(OngoingEventsFile);
        var existingEvent = events.Find(e => e.Title == title);
        if (existingEvent != null)
        {
            existingEvent.Date = newDate;
            existingEvent.Description = newDescription;
            EventStorage.SaveEvents(OngoingEventsFile, events);
        }
    }

    public static void DeleteEvent(string title)
    {
        var events = EventStorage.LoadEvents(OngoingEventsFile);
        events.RemoveAll(e => e.Title == title);
        EventStorage.SaveEvents(OngoingEventsFile, events);
    }

    public static void ListEvents()
    {
        var events = EventStorage.LoadEvents(OngoingEventsFile);
        foreach (var e in events)
        {
            Console.WriteLine($"{e.Title} on {e.Date:yyyy-MM-dd}: {e.Description}");
        }
    }
}
