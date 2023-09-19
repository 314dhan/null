def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    print("Welcome to the calculator app!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        result = add(num1, num2)
        print("Result:", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice!")

calculator()
