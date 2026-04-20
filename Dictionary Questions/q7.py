# count frequency
mystr = input("Enetr a str = ")

freq = {

}

for ch in mystr:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)