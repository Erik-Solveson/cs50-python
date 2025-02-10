from emoji import emojize

def main(): 
    phrase = input("input: ")
    converted_phrase = convert_to_emoji(phrase)
    print("output: ", converted_phrase)

def convert_to_emoji(phrase):
    try:
        phrase = emojize(phrase, language='alias')
        return phrase
    except:
        ("something went wrong")

main()
