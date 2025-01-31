# in/not in
L = [4,4,5,6,7,32434,564]

result = []
for num in L:
    if num not in result:
        result.append(num)
print(result)