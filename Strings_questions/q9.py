# write to reverse the order of words
mystr = "Hello World"

words = mystr.split()
result = []
n = len(words)
for i in range(n - 1 , -1 , -1 ):
    result.append(words[i])

ans = " ".join(ch for ch in result)
print(ans)
