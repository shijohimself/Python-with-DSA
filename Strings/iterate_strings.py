a = "Batman vs Superman"

# By index
n = len(a)
# for index in range(n):
#     print(a[index] , end = " ")

# iterate by value

for ch in a:
    print(ch , end = " ")

# print string in reverse
for index in range(n - 1 , -1 , -1 ):
    print(a[index])

for ch in a[::-1]:
    print(ch , end = " ")