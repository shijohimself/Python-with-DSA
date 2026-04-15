mystr = "Batman loves superman and fLASH"

words = mystr.split()

result = " ".join(i.capitalize() for i in words)
print(result)