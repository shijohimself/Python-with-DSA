my_list = [1.8,78,123,124,321,987,789,45,1211]

n = len(my_list)
# for i in range(1,n):
#     print(my_list[i])

# iteration by index
for i in range(n-1,-1,-1):
    print(my_list[i], end = " ")

# # Using range() to iterate over a list
# courses = ['java','python','pandas','sparks']
# for x in range(len(courses)):
#     print(courses[x])

print()
# print values in reverse
courses = ['java','python','pandas','sparks']
for x in range(len(courses)-1,-1,-1):
    print(courses[x])