# remove all even numbers
my_list = [45,66,66,66,66,78,11,11]
n = len(my_list)

for i in range(n - 1,-1,-1):
    if my_list[i] % 2 == 0:
        my_list.pop(i)
print(my_list)