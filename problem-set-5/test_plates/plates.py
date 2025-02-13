# This is a python program to validate a license plate in Massachusetts


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        contains_character_count(s)
        and contains_starting_letters(s)
        and contains_numbers(s)
        and contains_no_punctuation(s)
    ):
        return True
    else:
        #  print("you done messed up a-a-ron")
        return False


def contains_starting_letters(s):
    if not s[0].isalpha() or not s[1].isalpha():
        print("first two characters must be letters")
        return False
    else:
        return True


def contains_character_count(s):
    if len(s) <= 6 and len(s) >= 2:
        return True
    else:
        print("must be between 2 and 6 characters")
        return False


def contains_numbers(s):
    num = ""
    first_num = 0
    for i in range(len(s)):
        if s[i].isdigit():
            first_num = i
            if s[first_num] == "0":
                print("first number cannot be a 0")
                return False
            elif s[-1].isalpha():
                print("must contain numbers at the end")
                return False
            elif s[first_num:-1].isdigit():
                return True
        else:
            continue
    return True


def contains_no_punctuation(s):
    if s.isalnum():
        return True
    else:
        print("no punctuation allowed")
        return False


if __name__ == "__main__":
    main()

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     if (contains_character_count(s)
#     and contains_starting_letters(s)
#     and contains_numbers(s)
#     and contains_no_punctuation(s)):
#         return True
#     else:
#         #  print("you done messed up a-a-ron")
#          return False

# #checks if the first two characters are letters
# def contains_starting_letters(s):
#         if not s[0].isalpha() or not s[1].isalpha():
#             print("first two characters must be letters")
#             return False
#         else:
#              return True

# def contains_character_count(s):
#      if len(s) <= 6 and len(s) >= 2:
#         return True
#      else:
#         print("must be between 2 and 6 characters")
#         return False

# def contains_numbers(s):
#      num = ""
#      first_num = 0
#      for i in range(len(s)):
#           if s[i].isdigit():
#                first_num = i
#                if s[first_num] == "0":
#                     print("first number cannot be a 0")
#                     return False
#                elif s[-1].isalpha():
#                     print("must contain numbers at the end")
#                     return False
#                elif s[first_num: -1].isdigit():
#                     return True
#           else:
#                continue
#      return True


# def contains_no_punctuation(s):
#     if s.isalnum():
#          return True
#     else:
#          print("no punctuation allowed")
#          return False


# main()
