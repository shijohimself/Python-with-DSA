mydict = {
    "history" : 67,
    "computer" : 99,
    "science" : 78,
    "maths" : 87,
}
total = 0
for k in mydict.keys():
    total += mydict[k]
print(total)