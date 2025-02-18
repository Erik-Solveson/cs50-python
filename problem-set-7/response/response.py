import validators

def main():
    print(validate_email(input("please enter your email: ")))

def validate_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()