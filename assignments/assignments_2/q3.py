num = int(input("Enter your num: "))

if (num % 2 == 0 and num % 3 == 0) and  num % 8 != 0 :
    print(f"{num} is divisible by both 2 and 3 but not by 8!")
else:
    print("Inavalid")