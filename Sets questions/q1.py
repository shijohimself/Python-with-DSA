a = [1,2,3,4,5]
b = [4,5,6,7,8,9]

c = set(a)
d = set(b)

result_set = c.intersection(d)
print(result_set)

result_list = list(result_set)
print(result_list)