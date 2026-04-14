# BETTER APPROACH TO PREVIOUS QUESTION  
mystr = input("Enter input  - ")

for ch in mystr:
    is_upper = False
    is_lower = False
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        is_upper = True
    elif ascii >= 97 and ascii <= 122:
        is_lower = True

if is_lower == True and is_upper == False:
    print(f"{mystr} is lowercase")

