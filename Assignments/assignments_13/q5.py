L = [10,-5,8,3,-1,-9,7,2]

def interchange(lst):

    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp

interchange(L)
print(L)