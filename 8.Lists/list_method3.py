my_list = [2,2,2,2,"Shijo",7,True,False]

# my_list.append([2,4,5])
# my_list.append([1])
my_list.append(20) # only one positional arg
my_list.extend([1,2,3]) # extend expects iterable
print(my_list)

x = my_list.count(2)
print(x)

L = [2,3,4,5,2,7,1,4,3,2]
L.reverse() # only reverses the order
print(L)

L.sort()
print(L)
L.sort(reverse=True) # descending order
print(L)

