import csv
import sys

def main():
    in_file, out_file = intake_file()
    decode_csv(in_file, out_file)

# preforms error handling and returns the file names to open and write to.
def intake_file():
    try:
        if len(sys.argv) == 3:
            if sys.argv[1].rstrip().endswith(".csv") and sys.argv[2].rstrip().endswith(".csv"):
                return sys.argv[1], sys.argv[2]
            else: 
                print("files not .csv")
                sys.exit()
        else:
            print("incorrect number of command line arguments")
            sys.exit()
    except ValueError:
        print("there was a value error")
        sys.exit()
    


#opens and writes the csv's first column to a new file in two columns
def decode_csv(a, b):
    new_dict = []
    with open(a) as in_file:
        reader = csv.DictReader(in_file)  
        for line in reader:
            first_name, last_name = line["name"].split(',')
            house = line["house"]
            new_dict.append({"first_name": first_name.strip(), "last_name": last_name.strip(), "house": house.strip()})
    with open(b, 'w', newline="") as out_file:
        # print(new_dict)
        # print(f'this is new_dict of at 1 {new_dict[1]}')
        # print(f"this is the type of new_dict {type(new_dict)} and the type of new_dict at 1 {type(new_dict[1])}")
        writer = csv.DictWriter(out_file, fieldnames=["first_name", "last_name", "house"])
        for i in range(len(new_dict)):
            writer.writerow(new_dict[i])



if __name__ == "__main__":
    main()

