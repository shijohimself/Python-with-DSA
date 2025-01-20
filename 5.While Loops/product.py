n = int(input("Enter num = "))

def product(num):
    i = 1
    total = 1
    while i <= num:
        total *= i
        i += 1
    return total
print(product(n))
