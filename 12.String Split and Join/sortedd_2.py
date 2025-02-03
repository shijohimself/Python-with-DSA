my_list = [4,5,6,7,1,2,4,5,7,9,2,1]
print(id(my_list))

print("-".join(str(ch) for ch in sorted(my_list)))
print(id(my_list))
print(my_list)


print(sorted("HTERUYHGH#$$%&"))
#sort according to ascii value