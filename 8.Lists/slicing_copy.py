L = [1,2,3,4,5,6,7]
print(id(L))
# b = L
# print(id(b))

# L = [12,13,14]
# print(id(L)) # different id

L[:] = [12,13,14]
print(id(L))