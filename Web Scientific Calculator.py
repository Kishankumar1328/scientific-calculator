import streamlit as st
import math


# Calculator functions
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
        return "Cannot calculate square root"
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
    if x <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm"
    return math.log(x, base)


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


# Streamlit app
def main():
    st.title("Simple Calculator")

    operation = st.selectbox(
        "Select operation",
        ("Add", "Subtract", "Multiply", "Divide", "Exponential", "Square Root",
         "Modulus", "Factorial", "Logarithm", "Sine", "Cosine", "Tangent")
    )

    if operation in ("Add", "Subtract", "Multiply", "Divide", "Exponential", "Modulus"):
        num1 = st.number_input("Enter the first number")
        num2 = st.number_input("Enter the second number")

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Exponential":
        result = exponential(num1, num2)
    elif operation == "Modulus":
        result = modulus(num1, num2)
    elif operation == "Square Root":
        num = st.number_input("Enter the number")
        result = square_root(num)
    elif operation == "Factorial":
        num = st.number_input("Enter the number")
        result = factorial(num)
    elif operation == "Logarithm":
        num = st.number_input("Enter the number")
        base = st.number_input("Enter the base")
        result = logarithm(num, base)
    elif operation in ("Sine", "Cosine", "Tangent"):
        angle = st.number_input("Enter the angle in degrees")
        if operation == "Sine":
            result = sin(angle)
        elif operation == "Cosine":
            result = cos(angle)
        elif operation == "Tangent":
            result = tan(angle)

    st.write(f"Result: {result}")


if __name__ == "__main__":
    main()
