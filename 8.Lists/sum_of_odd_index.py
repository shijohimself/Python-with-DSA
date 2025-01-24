my_list = [1,2,3,4,5,6,7,8,24,76,87,98,123]

n = len(my_list)
total = 0
for i in range(0,n):
    if i % 2 != 0:
        total += my_list[i]
print(total)