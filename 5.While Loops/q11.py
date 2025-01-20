"""
368 -> factors -> total
"""
n = 368
def factors(num):
    i = 1
    total = num
    while i <= num//2:
        if num % i == 0:
            total += i
        i += 1
    return total
x = factors(n)
print(x)