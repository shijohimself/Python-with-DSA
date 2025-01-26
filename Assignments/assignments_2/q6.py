num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))
num4 = int(input("Enter num4 : "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"{num1} is greatest number of them all!")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"{num2} is greatest number of them all")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"{num3} is greatest of them all")
else:
    print(f"{num4} is greatest!")