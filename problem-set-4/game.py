import random


def main():
    number = get_input()
    play_game(number)


def get_input():
    while True:
        level = input("Enter a positive integer please: ")
        if level.isdigit() and int(level) > 0:
            return random.randint(0, int(level))
        else:
            print("invalid input")


def play_game(number):
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            if int(guess) == number:
                print("correct!")
                break
            elif int(guess) < number:
                print("higher")
            elif int(guess) > number:
                print("lower")

        else:
            continue


main()
