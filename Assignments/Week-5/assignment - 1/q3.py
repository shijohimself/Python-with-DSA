my_str = "sadvcvdSASADUYIUIKHKLguywewendk"

def remove_vowels(string):
    result = ""
    for ch in string:
        if ch not in 'aeiouAEIOU':
            result += ch
    return result

print(remove_vowels(my_str))

