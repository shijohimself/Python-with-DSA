from copy import deepcopy
a = [1,2,[3,4,5],6,7,8]

# b = a.copy()

# print(id(a))
# print(id(b))

# print(a)
# print(b)

# b[2][0] = 100
# # This will both change because of shallow copy
# print(a)
# print(b)

b = deepcopy(a)
print(id(a))
print(id(b))

print(a)
print(b)

b[0] = 100
b[2][0] = 100
print(a)
print(b)

