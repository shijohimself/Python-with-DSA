# count factors between 1 to 20
n = 12
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count += 1
    i += 1
print(count)
if count == 2:
    print(n, "is a prime number")



    
