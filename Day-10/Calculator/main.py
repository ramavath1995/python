logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def exponential(n1, n2):
    return n1 ** n2


operators = {"+": add,
             "-": subtract,
             "*": multiplication,
             "/": division,
             "**": exponential
             }
print(logo)


def calculator():
    num1 = int(input("\nEnter a first number: "))
    is_finished = False
    while not is_finished:
        for operator in operators:
            print(operator)

        oops = input(f"Select a operator: ")
        num2 = int(input("Enter second number: "))

        for operation in operators:
            if operation == oops:
                calculation = operators[operation]
                result = calculation(num1, num2)
                print(f"Answer is {result}")
                with_answer = input("Do you want to continue with answer? type yes/no or exit for end: ").lower()
                if with_answer == "yes" or with_answer == "y":
                    num1 = result
                elif with_answer == "no" or with_answer == "n":
                    calculator()
                elif with_answer == "exit":
                    is_finished = True


calculator()
