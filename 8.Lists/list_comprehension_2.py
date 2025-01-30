# L = [i for i in range(1,11) if i % 2 == 0]
# print(L)

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

L = [i for i in range(2,101) if is_prime(i)]
print(L)