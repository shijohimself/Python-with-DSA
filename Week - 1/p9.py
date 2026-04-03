start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

i = start
j = end

if i > j:
    while j <= i:
        print(j)
        j += 1
else:
    while i <= j:
        print(i)
        i += 1
print("Finished printing numbers from", start, "to", end)