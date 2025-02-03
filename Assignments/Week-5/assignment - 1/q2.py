my_str = "ahdashiweASA"
# x = my_str.upper()
# print(x)

def uppercase(string):
    result = ""
    for ch in string:
        asc = ord(ch)
        if asc >=97 and asc <= 122:
            asc -= 32
            result += chr(asc)
        else:
            result += ch
    return result

print(uppercase(my_str))

