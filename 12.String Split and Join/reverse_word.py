my_str = "python is a good language"

ans = my_str.split()
n = len(ans)
result = []

for index in range(n-1,-1,-1):
    result.append(ans[index])
print(result)

final = " ".join(ch for ch in result)
print(final)
