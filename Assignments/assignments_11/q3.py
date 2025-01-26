# n = len(my_list)
# for i in range(0,n):
#     factor = 0
#     for j in range(1,my_list[i]+1):
#         if my_list[i] % j == 0:
#             factor += 1
#     if factor == 2:
#         print(my_list[i], end = " ")

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
my_list = [4,8,6,5,3,12,1,7,6,2]

for num in my_list:
    if is_prime(num):
        print(num, end = " ")