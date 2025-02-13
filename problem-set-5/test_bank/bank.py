#This is a python script to return an apporpiate amount of cash in accordance 
#with the greetings given by the user. Subject to the immutable law passed down by
#one episode of seinfeld.

def main():
    greeting = input("What is the greeting? ")
    greeting = greeting.lower().lstrip().rstrip()
    print(value(greeting))


def value(greeting):
    if greeting.split()[0] == "hello":
        return "$0"
    elif greeting[0] == "h":# or greeting[0] == 'H':
       return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

# ==== This was my original bank.py ====
# def main():
#     greeting = input("What is the greeting? ")
#     greeting = greeting.lower().lstrip().rstrip()
#     if greeting.split()[0] == "hello":
#         print("$0")
#     elif greeting[0] == "h":
#         print("$20")
#     else:
#         print("$100")

# main()