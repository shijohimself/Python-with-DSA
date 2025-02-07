marks = {
    "history" : 90,
    "maths" : 100,
    "sst" : 70,
    "hindi" : 89,
    "english" : 94
}

for k in marks:
    print(f"Key = {k} and value = {marks[k]}")


total = 0
for k in marks:
    total += marks[k]

print(total)