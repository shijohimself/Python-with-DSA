my_list = [4,8,6,5,3,12,1,7,6,2]

n = len(my_list)
count = 0
for i in range(0,n):
    prime = True
    for j in range(2,my_list[i]):
        if my_list[i] % j == 0:
            prime = False
            break
    if prime == True:
        count += my_list[i]
print(count)