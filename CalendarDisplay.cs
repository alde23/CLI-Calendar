using System;
using System.Globalization;

public static class CalendarDisplay
{
    public static void ShowCalendar(int year, int month)
    {
        var firstDayOfMonth = new DateTime(year, month, 1);
        var daysInMonth = DateTime.DaysInMonth(year, month);
        var currentDay = firstDayOfMonth;

        Console.WriteLine($"\nCalendar for {CultureInfo.CurrentCulture.DateTimeFormat.GetMonthName(month)} {year}");
        Console.WriteLine("Sun Mon Tue Wed Thu Fri Sat");

        int dayOfWeek = (int)currentDay.DayOfWeek;
        for (int i = 0; i < dayOfWeek; i++)
        {
            Console.Write("    ");
        }

        for (int day = 1; day <= daysInMonth; day++)
        {
            Console.Write($"{day,3} ");
            if ((dayOfWeek + day) % 7 == 0)
            {
                Console.WriteLine();
            }
        }
        Console.WriteLine("\n");
    }
}
