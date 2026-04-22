# global scoping

def change():
    
    global a
    a = 30
    print(a)


a = 15

print(a)
change()
print(a)