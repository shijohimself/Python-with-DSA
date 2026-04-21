"""
ask 2 num from user
calculate sum of 2 num
print if sum is odd or even
"""

def add(n1,n2):
    sum = n1 + n2
    return sum

def check(num):
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")

num1 = int(input("enter num 1 = "))
num2 = int(input('enter num 2 = '))

add_sum = add(num1,num2)
print(add_sum)
check(add_sum)