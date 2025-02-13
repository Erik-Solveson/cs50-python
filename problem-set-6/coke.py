#This is a python script that will dynamically calculate the amount of change a
#user is owed from purchasing a coke.

def main():
    amount_due = 50
    amount_inserted = 0

    while True:
        print("Amount due: ", amount_due)
        amount_inserted = int(input("insert coin: "))
        #subtrect the amount only if the coin value is 5,10, or 25
        if (amount_inserted == 5 or amount_inserted == 10 or amount_inserted == 25) and amount_due > 0:
            amount_due -= amount_inserted
            if amount_due <= 0:
                break
        
            

    print("Change owed: ", amount_due*-1)

main()
