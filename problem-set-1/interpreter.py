#This is a python script that will do math for the user based on the inputs

def main():
    x, y, z = input("enter your expression: (x y z) ").split(" ")
    x = float(x)
    z = float(z)
    match y:
        case "+":
            print(x+z)
        case "-":
            print(x-z)
        case( "/"):
            print(x/z)
        case "*":
            print(x*z)

main()