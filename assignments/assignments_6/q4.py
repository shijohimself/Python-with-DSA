n = int(input("Enter input = "))
def pattern(num):
    i = 0
    count = 0
    while i < num:
        count = (count * 10) + 1
        i += 1
        print(count)
pattern(n) 
