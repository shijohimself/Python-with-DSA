my_list = [5,10,15,20,15]
new_list = []
n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        new_list.append(my_list[i])
print(new_list)
