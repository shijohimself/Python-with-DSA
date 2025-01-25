a = [1,2,3,4,5,6,7,8]

b = a.copy() # shallow copy

print(id(a))
print(id(b))

b[0] = 100
# here memory is copied so both will be changed
print(a)
print(b)

