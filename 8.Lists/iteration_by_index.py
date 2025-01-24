my_list = [1.8,78,123,124,321,987,789,45,1211]

n = len(my_list)
# for i in range(1,n):
#     print(my_list[i])

# iteration by index
for i in range(n-1,-1,-1):
    print(my_list[i], end = " ")