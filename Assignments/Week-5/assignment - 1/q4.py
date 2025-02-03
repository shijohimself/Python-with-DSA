my_str = "sadvcvdS ASADUYIUIKHKLguywewendk"
n = len(my_str)
print(n)
def count_num(string):
    words = 0
    spaces = 0
    for ch in string:
        asc = ord(ch)
        if (asc >= 65 and asc <= 90) or (asc >= 97 and asc <= 122):
            words += 1
        elif asc == 32:
            spaces += 1
    return words

print(count_num(my_str))