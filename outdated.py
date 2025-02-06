# This is a python script to convert dates entered in middle-endian order (MM/DD/YYYY)
# into ISO 8601 format()
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = input("Enter a date: ")
    if date[0].isdigit():
        month, day, year = date.split("/")
        print(f"{year}-{month}-{day}")
    elif date[0].isalpha():
        month, day, year = date.split(" ")
        day = day.strip(",")
        if int(day) > 31:
            print("Invalid date (too many days in a month)")
        elif month in months:
                print(f"{year}-{months.index(month)+1}-{day}")
        else:
                print("Invalid date (month not recognized)")


main()