#This is a python script that will tell the user when to eat!

def main():
    time = input("what time is it? ")
    ConvertedTime = convert(time)
    if ConvertedTime >=700 and ConvertedTime <= 800:
            print("breakfast time")
    elif ConvertedTime >=1200 and ConvertedTime <= 1300:
            print("lunch time")
    elif ConvertedTime >=1800 and ConvertedTime <= 1900:
            print("dinner time")
    else:
            print("not a mealtime, sorry!")

def convert(time):
    time = time.split(":")
    time = "".join(time)
    return float(time)

main()