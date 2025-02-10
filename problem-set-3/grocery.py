#This is a python script to record a grocery list of items that the user inputted
#It will then return a list of items with a quantity of each item

def main():
    grocery_dict = {}
    while True:
        try:
            # I needed to use ctrl+z to exit the loop since I'm on windows
            input_item = input("Enter an item or control-z to quit: ")
            if input_item in grocery_dict:
                grocery_dict[input_item] += 1
            elif input_item == "":
                break
            else: 
                grocery_dict.update({input_item: 1})
        except EOFError:
            break

    for i in grocery_dict.keys():
        print(f"{i} {grocery_dict[i]} ")
main()