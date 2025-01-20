"""
keep asking num until he press 0
"""
i = 1
total = 0
while True:
    num = int(input("Enter num: "))
    total = total + num
    print(total)
    if num == 0:
        break
    i+= 1