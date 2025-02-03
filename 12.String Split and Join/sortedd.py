my_list = [4,5,6,7,1,2,4,5,7,9,2,1]
print(id(my_list))
my_list.sort() # here the original list is changed
print("-".join(str(ch) for ch in my_list))
print(id(my_list))
print(my_list)
