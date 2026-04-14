lst = []
for i in range(0,11):
    num = int(input((f"enter num {i} = ")))
    lst.append(num)
print(lst)

lst2 = []
n = len(lst)
for i in range(n - 1 , -1 , -1 ):
    lst2.append(lst[i])
print(lst2)
