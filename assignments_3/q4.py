# simple calculator

n1 = int(input("n1: "))
n2 = int(input("n2: "))
operator = input("Enter op = ")

def simple_calculator(num1 , num2 , op):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
 
simple_calculator(n1,n2, operator)
