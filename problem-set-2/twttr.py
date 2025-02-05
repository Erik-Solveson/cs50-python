#This is a python script to take in a string and return a string without vowels

def main():
    input_string = input("Input: ")
    output_string = ""

    for i in range(len(input_string)):
        if input_string[i] not in ['a','e','i','o','u','A','E','I','O','U']:
            output_string += input_string[i]

    print("Output: ", output_string)

main()