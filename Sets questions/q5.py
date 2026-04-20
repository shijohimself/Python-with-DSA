set1 = {1,2,23,4}
set2 = {4,5,6,23}

result = set1.intersection(set2)

if len(result) == 0:
    print("both have nothing in common")
else:
    print("sets have a common element")
    print(result)