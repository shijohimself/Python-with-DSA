
my_list = [45,31,7,5,3,100,17,19,25,65,92]

prime_list = []
for num in my_list:
    is_factor = False
    for i in range(1,num):
        if num % i == 0:
            is_factor =True
    if is_factor == False:
        prime_list[num] += num
print(prime_list)
