from pyfiglet import Figlet
import sys
from fonts import get_random_font



def main():
    try:
        if len(sys.argv) == 1:
            #TODO add random figlet font
            print_with_figlet(get_random_font())
        elif len(sys.argv) == 3 and sys.argv[1] =='-f':
            print_with_figlet(sys.argv[2])
        else:
            # print(sys.argv)
            raise ValueError
    except:
        print("invalid usage")
        sys.exit

def print_with_figlet(font):
    f = Figlet(font = font)
    phrase = input("Enter text to be transformed: ")
    print(f.renderText(phrase))

main()