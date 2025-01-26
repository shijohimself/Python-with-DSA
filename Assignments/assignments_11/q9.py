my_list = [4,8,6,19,3,12,1,7,6,2]

for num in my_list:
    factor = 0
    for j in range(0,num + 1):
        if num % j == 0:
            factor += 1
    if factor == 2:
        print(num)