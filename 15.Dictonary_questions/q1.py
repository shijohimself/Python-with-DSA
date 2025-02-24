my_list = [1,2,2,3,4,5,6,6,7,7,7,7,7,4,3,2]

my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num,0) + 1

print(my_dict)

max_frequency = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_frequency:
        max_frequency = my_dict[key]
        max_element = key
print(max_element,max_frequency)