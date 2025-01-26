# find the sum of 3 digit num entered by user

num = int(input("num = "))
total = 0
for i in range(0,3):
    total += (num%10)
    num = num//10
    i += 1
print(total)
