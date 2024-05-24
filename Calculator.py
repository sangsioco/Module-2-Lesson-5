# Task 1 Create a functions for each arithmetic operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Task 2 Implement user input to receive numbers and an operation choice.

def get_user_input():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    return num1, num2, operation

def calculator():
    num1, num2, operation = get_user_input()
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

# Task 3 Ensure your program can handle division by zero and other potential errors.
    else:
        result = "Invalid operation!"
    print("Result:", result)

calculator()
