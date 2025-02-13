def main():
    fuel = input("Enter your fractional fuel amount: ")
    fuel_string = convert(fuel)
    output = gauge(fuel_string)
    print(output)

def convert(fuel):
    try:
        numerator, denominator = fuel.split("/")
        fuel = round(int(numerator) / int(denominator) *100)
        return fuel
    except ValueError:
        print(f"{fuel} is not a valid fraction")
    except ZeroDivisionError:
        print("You can't divide be zero or the universe will implode")

def gauge(fuel):
    if fuel <= 1 and fuel >=0:
        return("E")
    elif fuel >=99 and fuel <= 100:
        return("F")
    elif fuel > 100:
        return("your tank is overflowing!")
    else:
        return(f"{fuel}%")


if __name__ == "__main__":
    main()




#This is a python script that prompts the user for a fule amount as a fraction
#and the prints the result as a percentage, or else f or e (full and empty)
#If the user enters an invalid value, we also have error handling

# while True:
#     try:
#         fuel = input("Enter your fractional fuel amount: ")
#         numerator, denominator = fuel.split("/")
#         fuel = round(int(numerator) / int(denominator) *100)
        
#     except ValueError:
#         print(f"{fuel} is not a valid fraction")
#     except ZeroDivisionError:
#         print("You can't divide be zero or the universe will implode")

#     else:        
#         if fuel <= 1:
#             print("E")
#         elif fuel >=99 and fuel < 100:
#             print("F ",end="")
#         elif fuel > 100:
#             (print("your tank is overflowing!"))
#             continue
#         else:
#             print(f"{fuel}%")
#         break