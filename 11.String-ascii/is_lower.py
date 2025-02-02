def isLower(string):
    is_lower = False
    is_upper = False
    for ch in string:
        asc = ord(ch)
        if asc >= 97 and asc <= 122:
            is_lower = True
        elif asc >= 65 and asc <= 90:
            is_upper = True
    # if is_lower == True and is_upper == False:
    #     return True
    # return False
    if is_lower and not is_upper:
        return True
    return False

str = "dhjsdgA&^^(*&(*&))"
print(isLower(str))