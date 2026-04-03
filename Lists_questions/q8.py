# how many positive and negative numbers are there in the list
l1 = [11, 20, -33, 46, -55]
positive_count = 0
negative_count = 0
for i in l1:
    if i >0:
        positive_count = positive_count + 1
    elif i < 0:
        negative_count = negative_count + 1
print("Positive numbers count:", positive_count)
print("Negative numbers count:", negative_count)