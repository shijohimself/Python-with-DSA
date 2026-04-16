lst1 = ['Ten','Twenty','Thirty']
lst2 = [10,20,30]

mydict = {

}
n = len(lst1)
for i in range(n):
    mydict[lst1[i]] = lst2[i]

print(mydict)