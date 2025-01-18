"""
how many numbers are divisbile by 7
"""

st = int(input("start: "))
en = int(input("end: "))

i = st
count = 0
while i <= en:
    if i % 7 == 0:
        count += 1
    i += 1
print(count)

i = st
count = 0
while i <= en:
    if i % 7 == 0 and i % 2 == 0:
        count += 1
    i += 1
print(count)