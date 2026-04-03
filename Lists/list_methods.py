l1 = [12,13,14,15]
print(l1)

# l1.append(10)
# print(l1)

# l1.append(-1)
# print(l1)

l1.insert(1,32)
print(l1)

# remove by index
l1.pop()
print(l1)

#remove by value
l1.remove(13)
print(l1)

#can be used not only for list but for eveything
del l1[0]
print(l1)

# clears the entire list but List will not be deleted.
l1.clear()
print(l1)