#This is a python script that will output a number in joules that represents
# the energy of an item pre E = mc^2
def main():
    phrase = input("What is the mass of the item in kilograms? ")
    print(int(phrase)*300000000**2)

main()