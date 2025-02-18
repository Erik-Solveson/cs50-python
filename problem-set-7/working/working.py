import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    pattern = r"\b(?:\d{1,2}:\d{2} (?:AM|PM)|\d{1,2} (?:AM|PM))\b"
    matches = re.findall(pattern ,s)
    matches = twelve_hour_to_twentyfour_hour(matches)
    return (matches)


def twelve_hour_to_twentyfour_hour(matches: list[str]) -> str:
    """
    function that takes in a list of strings in 12-hour format and returns
    a list of strings in 24-hour format
    """
    for i in range(len(matches)):
        #ends wtih PM, add 12 to the hours and return in HH:MM format
        if matches[i].rstrip().endswith("PM"):
            time, meridiem = matches[i].split(" ")
            if len(time) == 4:
                hours, minutes = time.split(":")
                # print(hours)
                hours = str(int(hours)+12)
                matches[i] = hours + ":" + minutes
            else:
                hours = time
                matches[i] = hours + ":" + "00"
        #ends in AM, add no hours and return in HH:MM format
        else:
            time, meridiem = matches[i].split(" ")
            if len(time) == 4:
                hours, minutes = time.split(":")
            matches[i] = time
    return(matches)

if __name__ == "__main__":
    main()