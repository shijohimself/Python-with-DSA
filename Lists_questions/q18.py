num = int(input("enter value = "))
my_list = [1 , 2 , 3 , 4 , 5]
if num in my_list:
    index = my_list.index(num)
    print(index)
else:
    print(-1)
    