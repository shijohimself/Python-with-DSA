"""
my_str
"""

my_str = "dfshueywedhkj12235457 dh^%$&^&(*%&%)"
# count alphabets, digits, and symbols

alphabets = 0
digits = 0
symbols = 0
spaces = 0
for ch in my_str:
    asc = ord(ch)
    if (asc >= 65 and asc <= 90) or (asc >= 97 and asc <= 122):
        alphabets += 1
    elif asc >= 48 and asc <= 57:
        digits += 1
    elif asc == 32:
        spaces +=1
    else:
        symbols += 1
print(f"alphabets = {alphabets} , digits = {digits} , symbols = {symbols} , spaces = {spaces}")

