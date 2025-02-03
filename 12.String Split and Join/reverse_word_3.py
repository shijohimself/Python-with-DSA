my_str = "python is a good language"
# result -> egaugnal doog a si nohtyp

result = my_str.split()
print(result)
n = len(result)

result2 = []
for index in range(n-1,-1,-1):
    result2.append(result[index])
print(result2)

print(" ".join(ch[::-1] for ch in result2))