i = 5674
j = 10983
count = 0
total_2 = 0
while i <= j:
    if i % 2 == 0 and i % 7 == 0:
        total_2 += 1
    if i % 7 == 0:
        count += 1
    i += 1
print("Total numbers divisible by 7 between 5674 and 10983 are:", count)
print("Total numbers divisible by both 2 and 7 between 5674 and 10983 are:", total_2)