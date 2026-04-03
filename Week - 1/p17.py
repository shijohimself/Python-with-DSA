n = int(input("Enter a number: "))
i = 1
factorial = 1
total = 0
while i <= n:
    factorial = factorial * i
    total += i/factorial
    i += 1
print("Sequence sum is:", total)