my_list = [4,8,6,5,3,12,1,3,6]

n = len(my_list)
even = 0
odd = 0
for i in range(0,n):
    if my_list[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)
