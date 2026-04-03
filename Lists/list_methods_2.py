list1 = [55 , 65 , 100 , "Shijo" , True]

x = list1.index(55)
print(x) 

a = [10,15,16 , 17 ,19 , 1,3,5]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a.reverse()
print(a)

# This will append the whole list
a.append([21,"Stephen",False])
print(a)
a.extend([21,"Stephen",False])
print(a)

x = a.count(17)
print(x)