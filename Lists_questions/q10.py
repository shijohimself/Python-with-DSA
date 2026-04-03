# print all prime numbers from the list
l1 = [11, 20, 33, 46, 55, 7 , 13, 17, 34 , 52]
n = len(l1)
for i in range(n):
    factor = 0
    for j in range(1, l1[i]+1):
        if l1[i] % j == 0:
            factor = factor + 1
    if factor == 2:
        print(l1[i])