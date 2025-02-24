# Find the sum of all the elements in the list
myList = [1,2,3,4,5,6,7,8,9,4,5,6,2]

total = 0
n = len(myList)
for index in range(0,n):
    total += myList[index]
print(total)