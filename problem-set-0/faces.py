#This is a program to add emojis to a string when promted

# With an if statment checking for a specific string
# def main():
#     phrase = input("Please enter a phrase: ")
#     ConvertedPhrase = convert(phrase)
#     print(ConvertedPhrase)

# def convert(phrase):
#      if phrase == 'hello :)':
#         return 'hello, 🙂'
#      elif phrase == 'goodbeye :(':
#         return 'goodbye, 🙁'
#      else:
#          return phrase
     
# main()

#With the .convert string method
def main():
    phrase = input("Please enter a phrase: ")
    ConvertedPhrase = convert(phrase)
    print(ConvertedPhrase)

def convert(phrase):
    return phrase.replace(":)", "🙂").replace(":(", "🙁")

main()