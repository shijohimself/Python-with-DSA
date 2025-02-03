my_str = "python is a good language"

ans = my_str.split()
print(ans)

# print(" ".join(ch[::-1] for ch in ans))

result = ""
for word in ans:
    result += word[::-1]
    result += " "
print(result)
print(result[:-1])