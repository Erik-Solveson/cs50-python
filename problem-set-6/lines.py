import csv 

file_name = "coke.py"

def main():
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        i = 0
        for line in lines:
            if line.lstrip().startswith('#'):
                continue
            elif line.isspace():
                continue
            else:
                i += 1
        print(f"Threre are {i} lines of code in {file_name}")
    except FileNotFoundError:
        print("file not found")

if __name__ == "__main__":
    main()