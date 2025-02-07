my_list = [2,2,2,2,7,9,6,5,4,3,6,7,4,6]

"""
{
 frequency of every element
}
"""

my_dict = {}

for num in my_list:
    if num in my_dict:
        my_dict[num] = my_dict[num] + 1
    else:
        my_dict[num] = 1
print(my_dict)