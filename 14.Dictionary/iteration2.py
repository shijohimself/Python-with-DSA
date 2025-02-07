marks = {
    "history" : 90,
    "maths" : 100,
    "sst" : 70,
    "hindi" : 89,
    "english" : 94
}

# print(marks.keys())

# for k in marks.keys():
#     print(k)

# for v in marks.values():
#     print(v)

# print(marks.items())

result = marks.items()
print(list(result)[0][0])
print(list(result)[2][-1])