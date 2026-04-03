# menu driven program

fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = fnum + snum
    print("The sum is:", result)
elif op == '-':
    result = fnum - snum
    print("The difference is:", result)
elif op == '*':
    result = fnum * snum
    print("The product is:", result)
elif op == '/':
    if snum != 0:
        result = fnum / snum
        print("The quotient is:", result)
    else:
        print("Error: Division by zero is not allowed.")