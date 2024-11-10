from argparse import ArgumentParser

import calendar_utils as cu

calendar_ = cu.Calendar()
calendar_.load_events_from_file()


# Main parser for basic commands
# Sub parser for subcommands
main_parser = ArgumentParser()
sub_parser = main_parser.add_subparsers(dest="command")

# "add" command
add_parser = sub_parser.add_parser("add", help="Add event to calendar")

# required arguments for subcommands for the "add" command
add_parser.add_argument("title", type=str, help="Title of the event")
add_parser.add_argument("date", type=str, help="Date of the event in YYYY-MM-DD format")

# optional args
add_parser.add_argument("-d", "--description", type=str, help="Description of the event")
add_parser.add_argument("-t", "--time", type=str, help="Time of the event in HH:MM format")
add_parser.add_argument("-n", "--notification", type=str, help="Notification time for the event in YYYY-MM-DD-HH:MM format")


# "finish" command
finish_parser = sub_parser.add_parser("finish", help="Finish event with specified title and date")

# required args for "finish"
finish_parser.add_argument("title", type=str, help="Title of the event you want to finish")
finish_parser.add_argument("date", type=str, help="Date of the event you want to finish in YYYY-MM-DD format")


# "delete" command
delete_parser = sub_parser.add_parser("delete", help="Delete event with specified title and date")

# required args for "finish"
delete_parser.add_argument("title", type=str, help="Title of the event you want to delete")
delete_parser.add_argument("date", type=str, help="Date of the event you want to delete in YYYY-MM-DD format")


# "modify" command
modify_parser = sub_parser.add_parser("modify", help="Delete event with specified title and date")

# required args for "modify"
modify_parser.add_argument("title", type=str, help="Title of the event you want to modify")
modify_parser.add_argument("date", type=str, help="Date of the event you want to modify in YYYY-MM-DD format")

# optional args
modify_parser.add_argument("-d", "--description", type=str, help="Description of the event")
modify_parser.add_argument("-t", "--time", type=str, help="Time of the event in HH:MM format")
modify_parser.add_argument("-n", "--notification", type=str, help="Notification time for the event in YYYY-MM-DD-HH:MM format")


# "show" command
show_parser = sub_parser.add_parser("show", help="Show calendar")

# optional args of "show"
show_parser.add_argument("-y", "--year", help="Year you want shown")
show_parser.add_argument("-m", "--month", help="Month you want shown")


# "list" command
list_parser = sub_parser.add_parser("list", help="List events")

# optional args of "show"
list_parser.add_argument("-d", "--date", help="Date of events you want shown")

args = main_parser.parse_args()

if args.command == "list":
    cu.list_events("2024-11-15", calendar_.events)



