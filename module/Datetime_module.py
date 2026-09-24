import datetime
import time

def display_current_datetime():
    now = datetime.datetime.now()

    print("Current Date & Time:", now)
    print("---------------------------------------------------")


def calculate_date_difference():
    start_date = input("Enter start date and time (DD-MM-YYYY HH:MM:SS): " )

    end_date = input( "Enter end date and time (DD-MM-YYYY HH:MM:SS): " )

    start_date = datetime.datetime.strptime(
        start_date,
        "%d-%m-%Y %H:%M:%S"
    )

    end_date = datetime.datetime.strptime(
        end_date,
        "%d-%m-%Y %H:%M:%S"
    )

    difference = end_date - start_date

    print("Difference:", abs(difference))
    print("-------------------------------------------------")


def format_date():
    date = input("Enter date and time (YYYY-MM-DD): " )

    custom_date = datetime.datetime.strptime(
        date,"%Y-%m-%d"
    )

    print("Custom Format:", custom_date.strftime("%d-%m-%Y"))
    print("---------------------------------------------------")


def stopwatch():
    input("Press Enter to start the stopwatch...")

    start = time.time()

    input("Press Enter to stop the stopwatch...")

    end = time.time()

    difference = end - start

    print(f"Time elapsed: {difference:.2f} seconds")
    print("------------------------------------------------")


def countdown_timer():
    seconds = int(
        input(
            "Please enter the seconds from which you have to start the countdown timer :"
        )
    )

    while seconds > 0:
        print(seconds)

        time.sleep(1)

        seconds -= 1

    print("Time up!")
    print("-----------------------------------------------")





