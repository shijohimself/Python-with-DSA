my_str = "abaaabbbcdfgettttt"

def remove_duplicates(string):
    result = ""
    for ch in string:
        if ch not in result:
            result += ch
    return result

print(remove_duplicates(my_str))
