# count how many alphabets are there in a string

mystr = "dhaADDhjsdhg234234$##$#%"
count = 0
for ch in mystr:
    if (ord(ch) >= 65 and ord(ch) <= 90) or (ord(ch) >= 97 and ord(ch) <= 122):
        count += 1
print(count)