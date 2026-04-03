num = int(input("Enter a number: "))

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10

product = a + b + c
print("The sum of the digits is:", product)
