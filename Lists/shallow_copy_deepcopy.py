list1 = [1,2,4,3,5,6]
list2 = list1.copy() # shallow copy


print(id(list1))
print(id(list2))

list1.append(10)
print(list1)
print(list2)