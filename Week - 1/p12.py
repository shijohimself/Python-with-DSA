curr_pop = 10000
for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop = curr_pop/1.1
print("Before 10 years, population is:", int(curr_pop))