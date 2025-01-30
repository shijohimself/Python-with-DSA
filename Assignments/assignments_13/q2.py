L = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(id(L))
start = int(input("start = "))
end = int(input("end = "))

result = L[start:end]
print(result)
print(id(result))

