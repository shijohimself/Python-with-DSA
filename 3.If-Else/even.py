# ask an integer print even or odd

# num = int(input("Enter num: "))

# if num % 2 == 0:
#     print(f"Your num {num} is even number")
# else:
#     print(f"{num} is an odd number")


num = int(input("Enter num: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"Your num {num} is divisible by both")
else:
    print(f"{num} is not divisible!!")