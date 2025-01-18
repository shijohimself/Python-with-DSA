num = int(input("Enter num: "))

def sum_of_squares(n):
    i = 1
    count = 0
    while i <= n:
        count += i**2
        i += 1
    return count

x = sum_of_squares(num)
print(x)
