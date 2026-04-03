# Alternate method of solving prime number problem
def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
    
l1 = [10,20,30,7,13,17,21,23]
n = len(l1)
for i in range(n):
    if prime_num(l1[i]):
        print(l1[i])

    
