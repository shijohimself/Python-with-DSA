l1 = [1,2,3,4,5,6]
l2 = [8,9,20]
result = []
n1 = len(l1)
n2 = len(l2)
# list1 + list2 is also possible!
for i in range(n1):
    result.append(l1[i])
for i in range(n2):
    result.append(l2[i])

print(result)
