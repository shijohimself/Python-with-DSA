mydict = { "name" : "Shijo", 
           "age" : 23,
           "gender" : "Male",
           "marks" : [2,4,5,6],
           1:23
           }

r = mydict.get("namee")
print(r)

k = input("Enter key = ")
ans = mydict.get(k)

if ans is not None:
    print(ans)
else:
    print("key does not exists!")