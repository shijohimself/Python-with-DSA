my_str = "dhajksdhkigygeaweweuoi"


count = 0
for ch in my_str.lower():
    if ch in "aeiou":
        count += 1
print(count)
