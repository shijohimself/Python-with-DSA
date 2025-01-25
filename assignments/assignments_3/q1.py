# even odd

n = int(input("Enter your value = "))
def check_even_odd(x):
    if x % 2 == 0:
        print(f"{x} is an even number!")
    else:
        print("odd number!")

check_even_odd(n)