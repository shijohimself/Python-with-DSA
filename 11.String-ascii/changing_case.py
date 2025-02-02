my_str = 'ABSGADJKHabxcdfshf'

empty_str = ""
for ch in my_str:
    asc = ord(ch)
    if asc >= 97 and asc <= 122:
        asc -= 32
        empty_str += chr(asc)
    else:
        empty_str += ch
print(empty_str)
