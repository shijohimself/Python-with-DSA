#only alphanumeric characters
my_str = "ABA"

def checkAlphaNumeric(string):
    alphabets = False
    digits = False
    special_char = False
    for ch in string:
        asc = ord(ch)
        if (asc >=60 and asc <= 90) or (asc >=97 and asc <= 122):
            alphabets = True
        elif asc >= 48 and asc <= 57:
            digits = True
        else:
            special_char = True
    if alphabets == True and digits == True and special_char == True:
        return True

answer = checkAlphaNumeric(my_str)
if answer == True:
    print(f"{answer} Yes it is alphanumeric")
else:
    print("No it is not")
    