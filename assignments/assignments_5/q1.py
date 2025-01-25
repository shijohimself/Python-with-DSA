st = int(input("Enter num1: "))
en = int(input("enter num2: "))

if st <= en:
    i = st
    j = en
    total = 0
    while i <= j:
        total += i
        i += 1
    print(total)
else:
    i = en
    j = st
    total = 0
    while i <= j:
        total += i
        i += 1
    print(total)
