#remove non-alphabetic characters
my_str = "ABGASDHASsdhjsdgjh%^%&%&"

def remove_nonalpha(string):
    result = ""
    for ch in string:
        asc = ord(ch)
        if (asc >= 65 and asc <=90) or (asc >= 97 and asc <= 122):
            result += ch
    return result

print(remove_nonalpha(my_str))