import csv
import sys
from tabulate import tabulate

# FILE = "regular.csv"
# ALT_FILE = "sicilian.csv"


def main():

    try:
        if len(sys.argv) > 2:
            print("Too many command line arguments")
        elif not sys.argv[1].lower().endswith(".csv"):
            raise ValueError
        else:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                # print(type(reader.fieldnames))
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        print("file not found")
    except IndexError:
        print("command line argument not supplied")
    except ValueError:
        print("file not a csv")


if __name__ == "__main__":
    main()
