my_list = [45,31,7,5,3,100,17,19,25,65,92]

n = len(my_list)
for i in range(0,n):
    factor = 0
    for j in range(1,my_list[i]+1):
        if my_list[i] % j == 0:
            factor += 1
    if factor == 2:
        print(my_list[i] , end = " ")