L = [12,45,67,89,54]

n = int(input("Enter index = "))
def removeNth(lst,num):
    L2 = lst
    L3 = []
    length = len(L2)
    for i in range(0,length):
        if i != num:
            L3.append(L2[i])
    if num > length-1:
        return "Index is out of range"
    else:
        return L3
print(removeNth(L,n))

