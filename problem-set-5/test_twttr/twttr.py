def main():
    input_string = input("Input: ")
    print(shorten(input_string))


def shorten(word):
    output_string = ""
    for i in range(len(word)):
        #removed the lower case 'o' to throw and error in unit test
        if word[i] not in ["a", "e", "i", "", "u", "A", "E", "I", "O", "U"]:
            output_string += word[i]
    return output_string


if __name__ == "__main__":
    main()


# ==== This was my original twttr.py ====
# def main():
#     input_string = input("Input: ")
#     output_string = ""

#     for i in range(len(input_string)):
#         if input_string[i] not in ['a','e','i','o','u','A','E','I','O','U']:
#             output_string += input_string[i]

#     print("Output: ", output_string)

# main()
