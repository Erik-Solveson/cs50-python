from datetime import date
from datetime import timedelta
import sys
import inflect


def main():
    p = inflect.engine()
    # birthday = input("please enter your birthday in YYYY-MM-DD format: ")
    birthday = "jan 1, 1999"
    delta_in_min = calculate_time_delta(birthday)
    print(p.number_to_words(delta_in_min) + " minutes")



def calculate_time_delta(d):
    try:
        date1 = date.fromisoformat(d)
    except:
        print("invalid date")
        sys.exit()
    date2 = date.today()
    print(
        f"date1 is {date1} of type: {type(date1)}, timedelta is {date2} of type {type(date2)}"
    )
    date3 = date2 - date1
    return date3.days *1440


if __name__ == "__main__":
    main()
