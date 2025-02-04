my_set = {1,1,1,4,5,56,6,6,6,"Shijo",89.98}
print(my_set)

my_set.add(101)
print(my_set)

my_set.remove(1)
print(my_set)


my_set.clear()
print(my_set)

# another_set = my_set # it is copied by refrence
# another_set.add(100)
# print(my_set) 
# print(another_set)


another_set = my_set.copy()
another_set.add(100)
print(my_set) 
print(another_set)
