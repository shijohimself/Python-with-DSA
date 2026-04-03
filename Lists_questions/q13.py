my_list = [5,10,15,20,15]

old_num = int(input("Enter old num - "))
new_num = int(input("Enter new num - "))
n = len(my_list)
for i in range(n):
    if my_list[i] == old_num:
        my_list[i] = new_num
print(my_list)