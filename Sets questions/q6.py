set1 = {1,2,3,4}
set2 = {3,4,5,6}

common_elements = set1.intersection(set2)
print(common_elements)

for v in common_elements:
    set1.remove(v)
print(set1)
for v in common_elements:
    set2.remove(v)
print(set2)