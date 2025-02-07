my_list = [2,2,2,2,7,9,6,5,4,3,6,7,4,6]

my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num,0) + 1

print(my_dict)