# L = [i if i%2 == 0 else "odd" for i in range(1,11)]
# print(L)

# L2 = [f"even = {i}" if i%2 == 0 else f"odd = {i}" for i in range(1,11)]
# print(L2)


my_list = [34,23,56,74,33,77,83]

# ans = [num for num in my_list if num % 2 == 0]
# print(ans)

ans = [my_list[i] for i in range(0,len(my_list)) if my_list[i]% 2 == 0]
print(ans)