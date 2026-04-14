my_list = [1,2,17,3,7,8,6,12]
result = []

for num in my_list:
    factors = 0
    for i in range(1,num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        result.append(num)
print(result)