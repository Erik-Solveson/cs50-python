import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    pattern = r"\b(?:[1-9]|1[0-2]):[0-5][0-9] (?:AM|PM)|(?:[1-9]|1[0-2]) (?:AM|PM)\b"
    try:
        matches = re.findall(pattern ,s)
        print(matches)
        matches = twelve_hour_to_twentyfour_hour(matches)
        return matches[0] + " to " + matches[1]
    except ValueError:
        print("invalid time")
        sys.exit()
    except IndexError:
        print("Only one valid time")
        sys.exit()
    


def twelve_hour_to_twentyfour_hour(matches: list[str]) -> str:
    """
    function that takes in a list of strings in 12-hour format and returns
    a list of strings in 24-hour format
    """
    for i in range(len(matches)):
        #ends wtih PM, add 12 to the hours and return in HH:MM format
        if matches[i].rstrip().endswith("PM"):
            time, meridiem = matches[i].split(" ")
            # converts minutes if there is a :MM supplied
            if len(time) == 4:
                hours, minutes = time.split(":")
                hours = str(int(hours)+12)
                matches[i] = hours + ":" + minutes
                #add the ":))" if there are no minutes supplied
            else:
                hours = str(int(time)+12)
                matches[i] = hours + ":" + "00"
        #ends in AM, add no hours and return in HH:MM format
        else:
            time, meridiem = matches[i].split(" ")
            # converts minutes if there is a :MM supplied
            if len(time) == 4:
                hours, minutes = time.split(":")
                matches[i] = hours + ":" + minutes
                #add the ":))" if there are no minutes supplied
            else:
                matches[i] = time + ":" + "00"
    return(matches)

if __name__ == "__main__":
    main()