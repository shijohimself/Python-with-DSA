# take 3 input and print largest and smallest

num1 = int(input("Enter your num1: "))
num2 = int(input("Enter your num2: "))
num3 = int(input("Enter your num3: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greatest num!")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is greatest num!")
else:
    print(f"{num3} is greatest num!")
    
if num1 <= num2 and num1 <= num3:
    print(f"{num1} is smallest num!")
elif num2 <= num1 and num2 <= num3:
    print(f"{num2} is smallest num!")
else:
    print(f"{num3} is smallest num!")


# alt method - shortcuts
x = max(num1,num2,num3)
y = min(num1,num2,num3)
print(x , y)