my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25]

maxi = float("-inf")
n = len(my_list)
for i in range(0,n):
    maxi = max(maxi,my_list[i])
print(maxi)