""" 
Write a simple calculator (add, subtract, multiply, divide)
Requirements:
Handle division by zero
Ask user for two numbers and operation
Display result clearly
Allow multiple calculations
Exit when user chooses

"""

a = int(input("Enter first number:"))

b = int(input("Enter second number:"))

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error: can not divide bt zero!"
    return a/b



