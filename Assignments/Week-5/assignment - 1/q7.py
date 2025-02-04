my_str = "aeioughjklfghytrwq"

def replace_consonants(string):
    result = ""
    for ch in string:
        if ch in "aeiouAEIOU":
            result += ch
        else:
            result += "*"
    return result

print(replace_consonants(my_str))
