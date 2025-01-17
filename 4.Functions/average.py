# function named average
# 3 num from user -> cal avg

def average():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    num3 = int(input("num3: "))
    
    avg = (num1 + num2 + num3)/3
    print(f"{avg:.2f}")

average()