mydict = { "name" : "Shijo", 
           "age" : 23,
           "gender" : "Male",
           "marks" : [2,4,5,6],
           1:23
           }

print(mydict)

#method - 1
mydict['age'] = 25 # if key is there it will update
print(mydict) 
mydict['xyz'] = 32 # if key is not there it will add
print(mydict)

# method - 2
mydict.update({"nationality": "india" , "name" : "Batman"})
print(mydict)