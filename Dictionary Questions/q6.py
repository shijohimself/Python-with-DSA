mydict = {
    "history" : 67,
    "computer" : 99,
    "science" : 78,
    "maths" : 87,
}
total = 0
# for k,v in mydict.items():
#     total += v
# print(total)

for i in mydict:
    total += mydict[i]
print(total)