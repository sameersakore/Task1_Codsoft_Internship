
#        TASK1 : CALCULATOR 

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return float(x / y)

def calculator():
    print("************ CALCULATOR ***************\n")
    print("Select operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division \n")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print("\nResult Of Addition is :", addition(num1, num2))
    elif choice == '2':
        print("\nResult Of Subtraction is :", subtraction(num1, num2))
    elif choice == '3':
        print("\nResult Of Multiplication is :", multiplication(num1, num2))
    elif choice == '4':
        print("\nResult Of Division is :", divide(num1, num2))
    else:
        print("Invalid input")

calculator()


