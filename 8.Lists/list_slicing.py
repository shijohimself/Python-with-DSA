
L = [10,32,34,65,76,132,21,33,45,65,34]

# x = L[0:11:2]

# x = L[0:]
# x = L[3:]
# x = L[::3]
x = L[::2]

L2 = [10,32,34,65,76,132,21,33,45,65,34]
n = len(L2)
first_half = L2[:n//2]
seond_half = L2[n//2:]
full_list = first_half + seond_half
print(full_list)


