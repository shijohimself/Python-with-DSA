my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25]

mini = float("inf")
n = len(my_list)
for i in range(0,n):
    if my_list[i] < mini:
        mini = my_list[i]
print(mini)