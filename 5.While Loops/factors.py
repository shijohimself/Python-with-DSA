n = int(input('Enter value = '))
# def print_factors(num):
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             print(i, end = " ")
#         i += 1
# print_factors(n)

def print_factors_2(num):
    i = 1
    while i <= num//2:
        if num % i == 0:
            print(i , end = " ")
        i += 1
    print(num)
print_factors_2(n)
        