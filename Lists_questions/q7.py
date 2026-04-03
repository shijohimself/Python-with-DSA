# sum of all the even numbers in the list
l1 = [11, 20, 33, 46, 55]
n = len(l1)
sum = 0
for i in range(n):
    if l1[i] % 2 == 0:
        sum = sum + l1[i]
print(sum)