my_string = "ABVCFDJDHadssdferhg"


count = 0
count1 = 0
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        count += 1
    elif ascii_code >= 65 and ascii_code <= 90:
        count1 += 1 
print(f"lowercase letters = {count}")
print(f"uppercase letters = {count1}")