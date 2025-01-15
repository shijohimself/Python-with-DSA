name = "Shijo"
age = 23
gender = "male"

print("My name is",name)
print("My age is" , age)
print("My gender is", gender)

print("my name is",name,"My age is",age, "My gender is",gender)

#method-2 (f-strings)
print(f"my name is {name} and my gender is {gender}")

#method-3 (identifiers)
# """
# %s -> string
# %d -> integer
# %f -> float
# """
print("My name is %s" % name)
print("My age is %d" % age)
print("My name is %s and my age is %d" % (name,age))

