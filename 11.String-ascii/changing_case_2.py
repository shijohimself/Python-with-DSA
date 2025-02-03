# swapcase
my_str = "ASBHJAGHJDGs dasdjbjkahsh *&^*&(5687;;;866[])"

result = ''
for ch in my_str:
    asc = ord(ch)
    if asc >= 65 and asc <= 90:
        asc += 32
        result += chr(asc)
    elif asc >= 97 and asc <= 122:
        asc -= 32
        result += chr(asc)
    else:
        result += ch
print(result)
