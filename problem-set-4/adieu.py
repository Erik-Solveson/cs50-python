import inflect 
import sys

p = inflect.engine()

def main():
    names = []
    try:
        while True:
            input_name = input("enter a name to be added or crtl+z to exit: ")
            names.append(input_name)
            print("Adieu, adieu, to" , p.join((names), conj="and", sep="," ))
    except EOFError:
        sys.exit()
main()