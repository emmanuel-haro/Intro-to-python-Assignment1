# Simple calculator program
def calculator():
    # Taking user input for the first number, second number, and operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Performing the calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation"

    # Printing the result
    print(f"{num1} {operation} {num2} = {result}")

# Calling the function to run the program
calculator()
