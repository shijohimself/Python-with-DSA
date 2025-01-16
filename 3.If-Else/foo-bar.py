num = int(input("Enter your num: "))

if num % 3 == 0 and num % 5 == 0:
    print("FOO-BAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("Inavlid")