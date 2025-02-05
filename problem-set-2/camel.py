#This is a python script that will change a variable name from camelCase to snake_case

def main():
    camelCaseVariable = input("What is your variable name? ")
    snake_case_variable = ""
    
    for i in range(len(camelCaseVariable)):
        if camelCaseVariable[i].isupper():
            snake_case_variable += "_" + camelCaseVariable[i].lower()
        else: 
            snake_case_variable += camelCaseVariable[i]
    print(snake_case_variable.lstrip("_"))

main()