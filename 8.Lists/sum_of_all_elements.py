my_list = [1,2,3,4,5,6,7,8,24,76,87,98,123]

n = len(my_list)
count = 0
for i in range(0,n):
    count += my_list[i]
print(count)

total = 0
for i in my_list:
    total += i
print(total)
