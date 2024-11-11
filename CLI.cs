using System;
using System.Globalization;

public class CLI
{
    public static void Run()
    {
        bool running = true;

        while (running)
        {
            Console.WriteLine("");
            Console.WriteLine("Enter a command (add, modify, delete, list, calendar, exit):");
            var command = Console.ReadLine();

            if (string.IsNullOrEmpty(command))
            {
                Console.WriteLine("Command can't be empty");
                continue;
            }

            switch (command.ToLower())
            {
                case "add":
                    Console.Write("Title: ");
                    var title = Console.ReadLine();
                    if (string.IsNullOrEmpty(title))
                    {
                        Console.WriteLine("Title can't be empty");
                        continue;
                    }

                    Console.Write("Date(yyyy-MM-dd): ");
                    var dateInput = Console.ReadLine();
                    if (string.IsNullOrEmpty(dateInput) || !DateTime.TryParseExact(dateInput, "yyyy-MM-dd", CultureInfo.InvariantCulture, DateTimeStyles.None, out var date))
                    {
                        Console.WriteLine("Invalid date format. Use yyyy-MM-dd!");
                        continue;
                    }

                    Console.Write("Description: ");
                    var description = Console.ReadLine() ?? string.Empty;

                    EventManager.AddEvent(title, date, description);
                    Console.WriteLine("Event added successfully.");
                    break;

                case "modify":
                    Console.Write("Title of event to modify: ");
                    var modTitle = Console.ReadLine();
                    if (string.IsNullOrEmpty(modTitle))
                    {
                        Console.WriteLine("Title can't be empty.");
                        continue;
                    }

                    Console.Write("New Date (yyyy-MM-dd): ");
                    var newDateInput = Console.ReadLine();
                    if (string.IsNullOrEmpty(newDateInput) || !DateTime.TryParseExact(newDateInput, "yyyy-MM-dd", CultureInfo.InvariantCulture, DateTimeStyles.None, out var newDate))
                    {
                        Console.WriteLine("Invalid date format. Use yyyy-MM-dd!");
                        continue;
                    }

                    Console.Write("New Description: ");
                    var newDescription = Console.ReadLine() ?? string.Empty;

                    EventManager.ModifyEvent(modTitle, newDate, newDescription);
                    Console.WriteLine("Event modified successfully");
                    break;

                case "delete":
                    Console.Write("Title of event to delete: ");
                    var delTitle = Console.ReadLine();
                    if (string.IsNullOrEmpty(delTitle))
                    {
                        Console.WriteLine("Title can't be empty");
                        continue;
                    }

                    EventManager.DeleteEvent(delTitle);
                    Console.WriteLine("Event deleted successfully");
                    break;

                case "list":
                    Console.WriteLine("Listing all events:");
                    EventManager.ListEvents();
                    break;

                case "calendar":
                    Console.Write("Enter year: ");
                    var yearInput = Console.ReadLine();
                    if (string.IsNullOrEmpty(yearInput) || !int.TryParse(yearInput, out var year) || year < 1)
                    {
                        Console.WriteLine("Invalid year");
                        continue;
                    }

                    Console.Write("Enter month(1-12): ");
                    var monthInput = Console.ReadLine();
                    if (string.IsNullOrEmpty(monthInput) || !int.TryParse(monthInput, out var month) || month < 1 || month > 12)
                    {
                        Console.WriteLine("Invalid month");
                        continue;
                    }

                    CalendarDisplay.ShowCalendar(year, month);
                    break;

                case "exit":
                    running = false;
                    Console.WriteLine("Exiting program");
                    break;

                default:
                    Console.WriteLine("Unknown command");
                    break;
            }
        }
    }
}
