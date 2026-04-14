# make a list of your won and remove all the duplicate elements from that List
my_list = [5 ,1 , "Shijo", 56.32 , 5 , 5 , "Batman" , 1 , 1 , "Batman"]

result = []
for i in my_list:
    if i not in result:
        result.append(i)
print(result)