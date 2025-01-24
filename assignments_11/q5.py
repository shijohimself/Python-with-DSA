my_list = [4,8,6,5,3,12,1,7,6,2]

n = len(my_list)
list_sum = 0
product = 1
for i in range(0,n):
    list_sum += my_list[i]
    product *= my_list[i]
print(list_sum)
print(product)
