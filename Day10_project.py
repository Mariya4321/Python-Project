import calc_ascii


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    print(calc_ascii.logo)
    first_number = float(input("What's the first number: "))
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    for symbol in operators:
        print(symbol)
    is_continue = True

    while is_continue:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("Enter next number: "))
        calc = operators[operation_symbol]
        ans = calc(first_number, next_number)
        print(ans)

        continue_calc = input("Type 'y' to continue, type 'n' start from beginning and type 'e' to exit: ").lower()
        if continue_calc == 'y':
            first_number = ans
        elif continue_calc == 'n':
            calculator()
        else:
            is_continue = False


calculator()
