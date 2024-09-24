# from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    # print(logo)
    continue_calculation = True
    first_num = float(input("What's the first number?: "))

    while continue_calculation:
        for sign in calculation:
            print(sign)
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))
        answer = calculation[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {answer}")

        want_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()

        if want_to_continue == "y":
            first_num = answer
        else:
            continue_calculation = False
calculator()




