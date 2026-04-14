# ask a string and then print the ans whether it is lowercase?
# if there is no alphabet then this will show true
# wrong code
mystr = input("Enter input  - ")

for ch in mystr:
    lower = True
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        lower = False
if lower == True:
    print(f"{mystr} is lowercase")
else:
    print(f"{mystr} contains maybe upercase")
