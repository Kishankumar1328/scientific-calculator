import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def exponential(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot calculate square_root"
    return math.sqrt(x)

def modulus(x, y):
    if y == 0:
        return "Cannot perform modulus"
    return x % y

def factorial(x):
    if x < 0:
        return "Cannot calculate factorial for negative values"
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def logarithm(x, base):
    if x <= 0:
        return "Cannot calculate logarithm of non-positive number"
    if base <= 0 or base == 1:
        return "Base of logarithm must be positive and not equal to 1"
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def pi_value():
    return math.pi

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponential")
print("6. Square Root")
print("7. Modulus")
print("8. Factorial")
print("9. Logarithm")
print("10. Sine")
print("11. Cosine")
print("12. Tangent")
print("13. Pi")

while True:
    choice = input("Enter the choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

    if choice in ('1', '2', '3', '4', '5', '7'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    elif choice == "5":
        print("Result:", exponential(num1, num2))
    elif choice == "7":
        print("Result:", modulus(num1, num2))
    elif choice in ("6", "8", "9"):
        num1 = float(input("Enter the number: "))
        if choice == "6":
            print("Result:", square_root(num1))
        elif choice == "8":
            print("Result:", factorial(num1))
        elif choice == "9":
            base = float(input("Enter the base: "))
            print("Result:", logarithm(num1, base))
    elif choice in ("10", "11", "12"):
        angle = float(input("Enter the angle in degrees: "))
        if choice == "10":
            print("Result:", sin(angle))
        elif choice == "11":
            print("Result:", cos(angle))
        elif choice == "12":
            print("Result:", tan(angle))
    elif choice == "13":
        print("Value of Pi:", pi_value())

    again = input("Do you want to perform another calculation? (YES/NO): ")
    if again.lower() != "yes":
        break
