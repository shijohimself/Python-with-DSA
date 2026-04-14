mystr = "dhaADDhjsdhg234234$##$#%"

uppercase = 0
lowercase = 0

for ch in mystr:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        lowercase += 1
    elif ascii >= 65 and ascii <= 90:
        uppercase += 1
print(f"uppercase = {uppercase} and lowercase = {lowercase}")