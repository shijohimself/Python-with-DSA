L = [4,5,6,7,4,4,7,3]

my_dict = {}
for num in L:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1
print(my_dict)