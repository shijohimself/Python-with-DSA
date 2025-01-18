start = int(input("num1 = "))
end = int(input("num2 = "))

if start <= end:
    i = start
    while i <= end:
        print(i, end = " ")
        i += 1
else:
    i = end
    while i <= start:
        print(i , end = " ")
        i += 1
print()
print("Done!")