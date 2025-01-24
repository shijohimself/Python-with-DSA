my_list = [4,8,6,5,3,12,1,7,6,2]

n = len(my_list)
count = 0
for i in range(0,n):
    factor = 0
    for j in range(1,my_list[i]+1):
        if my_list[i] % j == 0:
            factor += 1
    if factor == 2:
        count += my_list[i]
print(count)