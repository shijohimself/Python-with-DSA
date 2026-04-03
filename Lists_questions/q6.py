# count the number of even numbers in the list
l1 = [11, 20, 33, 46, 55]
n = len(l1)
count = 0
for i in range(n):
    if l1[i] % 2 == 0:
        count = count + 1
print(count)