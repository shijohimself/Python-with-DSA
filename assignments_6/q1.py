num = int(input("Enter your num: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        i = 1
        count = 1
        while i <= n:
            count *= i
            i += 1
        return count

print(factorial(num))
