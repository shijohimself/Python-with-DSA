n = int(input("number = "))
def total_cups(num):
    cups = num//6
    total_cup = num + cups
    return total_cup

x = total_cups(n)
print(x)