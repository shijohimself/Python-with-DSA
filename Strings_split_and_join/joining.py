mylist = ["abc","bca","cab","d"]

print(mylist)

mystr = " ".join(mylist)
print(mystr)

mylist2 = ["abc","bac","cba","dub", 78]

mystr2 = " ".join(str(ch)[::-1] for ch in mylist2)
print(mystr2)