mydict = {
    "history" : 67,
    "computer" : 99,
    "science" : 78,
    "maths" : 87,
}
print(mydict.items())
for k,v in mydict.items():
    print(f"{k} = {v}")