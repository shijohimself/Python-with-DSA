num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
num3 = int(input("num3 = "))
num4 = int(input("num4 = "))

def avg(n1,n2,n3):
    average = (n1 + n2 + n3)
    return average/3

def check_large(avg_value,num):
    if avg_value >= num:
        return True
    return False

x = avg(num1,num2,num3)
print(check_large(x,num4))