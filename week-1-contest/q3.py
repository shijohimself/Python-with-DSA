n1 = int(input("n1: "))
n2 = int(input("n2: "))

op = input("Enetr the operator: ")

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print("Invalid operator")