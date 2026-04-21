def greet():
    name = input("enter your name - ")
    print(name)

name = "xyz" # this will also print bcoz of scoping
greet()
print(name)