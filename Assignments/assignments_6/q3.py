n = int(input("Enter your num = "))

def pattern(num):
    i = 0
    while i < num:
        print(2**i)
        i += 1
pattern(n)