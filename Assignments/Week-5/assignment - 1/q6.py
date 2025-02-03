my_str = "kdhksah sdhskd adshjlks udwui"

def capital(string):
    n = len(string)
    result = ""
    for index in range(0,n):
        asc = ord(string[index])
        if string[index] == 0:
            asc -= 32
            result += chr(asc)
        elif asc == 32:
            asc = string[index+1] - 32
            result += chr(asc)
    return result

print(capital(my_str))


