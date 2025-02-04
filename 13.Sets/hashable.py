# set can include those items
# which are hashable
# hashable -> immutable

print(hash(45.67))
# print(hash([12,23,5])) # this cant be done because list is mutable

set1 = {1,2,"Shijo",(12,13,14),78.456}
print(set1)