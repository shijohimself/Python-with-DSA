my_str = "dhajskdj askdhkjh oasidhjoi sdh"

def changeSpaces(string):
    result = ""
    for ch in string:
        asc = ord(ch)
        if asc == 32:
            result += "-"
        else:
            result += ch
    return result

print(changeSpaces(my_str))
