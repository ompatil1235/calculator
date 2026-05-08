# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
print("*"*45)
print("wellcome to my first project")
print("*"*45)
print("")



print("aapko kya krna hei:)")
print("")
print("a. Adding")
print("a. Subtracting")
print("c. Multiplying")
print("d. Divideing")
print("")


choice = input("Enter choice (a/b/c/d): ")

if choice in ['a', 'b', 'c', 'd']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'a':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == 'b':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == 'c':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == 'd':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    print("thank you for using me :)")
    print("have a nice day :)")
else:
    print("Invalid input")

