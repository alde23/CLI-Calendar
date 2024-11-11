using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

public static class EventStorage
{
    public static List<Event> LoadEvents(string filePath)
    {
        if (!File.Exists(filePath)) return new List<Event>();
        var json = File.ReadAllText(filePath);
        return JsonConvert.DeserializeObject<List<Event>>(json) ?? new List<Event>();
    }

    public static void SaveEvents(string filePath, List<Event> events)
    {
        var json = JsonConvert.SerializeObject(events, Formatting.Indented);
        File.WriteAllText(filePath, json);
    }
}
