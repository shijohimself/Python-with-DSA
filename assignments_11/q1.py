my_list = [4,8,6,5,3,12,1,3]

n = len(my_list)
count = 0
for i in range(0,n):
    if my_list[i] % 2 != 0:
        count += 1
print(count)
