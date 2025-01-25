my_list = [4,5,3,1,7,6,5,9,100]

# by index
n = len(my_list)
for i in range(0,n):
    if my_list[i] % 2 == 0:
        my_list[i] += 5
print(my_list)