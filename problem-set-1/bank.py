#This is a python script to return an apporpiate amount of cash in accordance 
#with the greetings given by the user. Subject to the immutable law passed down by
#one episode of seinfeld.

def main():
    greeting = input("What is the greeting? ")
    greeting = greeting.lower().lstrip().rstrip()
    if greeting.split()[0] == "hello":
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")

main()