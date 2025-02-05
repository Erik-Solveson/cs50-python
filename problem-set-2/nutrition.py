# This is a python program that reads the user's choice of fruit and 
# prints the corresponding calories

def main():
    fruitdict = {"apple": 130,
                 "Avaocado": 50,
                 "banana": 110,
                 "cantaloupe": 50,
                 "grapefruit": 60,
                 "grapes": 90,
                 "honeydew melon": 50,
                 "kiwifruit": 90,
                 "lemon": 15,
                 "lime": 20,
                 "nectarine": 60,
                 "orange": 80,
                 "peach": 60,
                 "Pear": 100,
                 "pinapple": 50,
                 "plums": 70,
                 "strawberries": 50,
                 "sweet cherries": 100,
                 "tangerine": 50,
                 "watermelon": 80
                 }
    
    fruit = input("Item ").lower()
    if fruit in fruitdict:
       print("Calories" ,fruitdict[fruit])
    else:
        print(end="")

main()