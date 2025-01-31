a = "SHIJO"
b = "shijo"
c = "abc"
d = "ABcdX8 9097"
e = "12354"
print(a.isupper())
print(b.isupper())
print(b.islower())
print(c.isalpha())
print(d.isalnum())
print(e.isdigit())



num = input("Enter num = ")
if num.isdigit():
    print(int(num))
else:
    print("error")