n = int(input("Enter your value = "))
def pattern(num):
    i = 1
    count = 0
    while i <= num:
        count = (count * 10) + 2
        i += 1
        print(count)
pattern(n)
