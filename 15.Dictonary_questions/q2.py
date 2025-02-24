my_str = "sthfjkjeyreuirhhhhhdfiyereeee"

my_dict = {}

for ch in my_str:
    my_dict[ch] = my_dict.get(ch,0) + 1

print(my_dict)

max_occurence = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_occurence:
        max_occurence = my_dict[key]
        max_element = key
print(max_element)
print(max_occurence)