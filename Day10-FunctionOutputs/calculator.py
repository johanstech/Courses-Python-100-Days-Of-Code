import os
from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    os.system("cls")
    print(logo)
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    calculating = True
    while calculating:
        operation_symbol = input("Enter operation symbol: ")
        num2 = float(input("Enter second number: "))
        operation = operations[operation_symbol]
        result = operation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        again = input(
            f"Keep calculating with {result}? (yes/no)\nType 'exit' to quit.\n").lower()
        if again == "yes":
            num1 = result
        elif again == "no":
            calculator()
        else:
            calculating = False


calculator()
