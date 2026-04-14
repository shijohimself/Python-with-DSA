list1 = [1,2,3,4,4,5]
list2 = [3,4,5,6,7]

result = []

for num in list1:
    if num in list2:
        if num not in result:
            result.append(num)
print(result)