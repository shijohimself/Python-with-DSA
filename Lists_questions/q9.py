# largest element in the list
l1 = [11, 20, 33, 46, 55, 32]
n = len(l1)
largest = l1[0]
for i in range(n):
    if l1[i] > largest:
        largest = l1[i]
print("Largest element:", largest)

