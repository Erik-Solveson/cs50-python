#This python program answers in the affimative if the user answers the 
#great question of life , the universe and everything with 42. Otherwise
#no.

def main():
    answer = input("what is the answer to the Great Question of Life the Universe and Everything? ")
    answer = answer.lower()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("yes")
    else:
        print("no")

main()