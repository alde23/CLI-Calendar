# CLI Calendar

CLI Calendar is a command-line interface (CLI) application for managing events. It allows users to add, modify, delete, finish, and list events, as well as display a calendar.

## Project Goals

The goal of this project is to provide a simple and efficient way to manage events directly from the command line. It is designed to be lightweight and easy to use, making it ideal for users who prefer using the terminal over graphical user interfaces.

## Features

- Add events with title, date, description, time, and notification.
- Modify existing events.
- Delete events.
- Mark events as finished.
- List events for a specific date.
- Show a calendar for a specific month or year.

## Technologies Used

- Python 3.6+

 for command-line argument parsing
- 
- argparse



 for data storage
- 
- json

 for date and time manipulation
- 
- datetime


 for displaying calendars
- 
- calendar


 for notifications (Windows only)
-
- win11toast

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/finalnirepo/cli-calendar.git
    cd cli-calendar
    ```

2. Ensure you have Python 3.6+ installed.

3. Install required dependencies:
    ```sh
    pip install win11toast
    ```

## Usage

Run the 

cli_calendar.py

 script with the desired command and arguments.

### Commands

#### Add Event

```sh
python cli_calendar.py add "Event Title" "2024-11-15" -d "Description" -t "09:00" -n "2024-11-15-07:00"
```

#### Finish Event

```sh
python cli_calendar.py finish "Event Title" "2024-11-15"
```

#### Delete Event

```sh
python cli_calendar.py delete "Event Title" "2024-11-15"
```

#### Modify Event

```sh
python cli_calendar.py modify "Event Title" "2024-11-15" -d "New Description" -t "10:00" -n "2024-11-15-08:00" -m "New Title" -s "2024-11-16"
```

#### Show Calendar

```sh
python cli_calendar.py show -y 2024 -m 11
```

#### List Events

```sh
python cli_calendar.py list -d "2024-11-15"
```

## Project Structure

```
.
├── __pycache__/
├── .idea/
│   ├── CLI Calendar Rebuild.iml
│   ├── inspectionProfiles/
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   ├── vcs.xml
│   └── workspace.xml
├── cli_calendar.py
├── cli_utils.py
├── notification_utils.py
├── data/
│   ├── events.json
│   └── finished.json
```


Enjoy using CLI Calendar!