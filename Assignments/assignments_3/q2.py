# n1 div by n2 or not

a = int(input("Enter num1 = "))
b = int(input("Enter num2 = "))
def check_div(num1 , num2):
    if num1 % num2 == 0:
        print("True!")
    else:
        print("False!")

check_div(a, b)