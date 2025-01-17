"""
scoping in python
"""

def info():
    # local variable!
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)

def greet():
    name = "Shijo"
    print(f"{name} good morning!")

info()
greet()