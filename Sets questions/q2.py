list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = [7,8,9,10,5]

result1 = set(list1).intersection(set(list2))
result = result1.intersection(set(list3))
print(list(result))