#This is apython script to implement a program that takes a user's order
# and prints out the cost of the order so far.

menu_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def main():
    order_total = 0
    try:
        while True:
            order = input("Item: ").title()
            order_total += validate_order(order)
    except EOFError:
        print(f"{order_total:.2f}")
    
def validate_order(order):
    if order in menu_prices:
        return menu_prices[order]
    else:
        print("not on the menu")

main()