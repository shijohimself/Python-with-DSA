mystr = "dhaADDhjsdhg234234$##$#%"
result = ""
for ch in mystr:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        ascii -= 32
        result += chr(ascii)
    elif ascii >= 65 and ascii <= 90:
        result += chr(ascii)
print(result)