n = int(input("Enter a value = "))
def count_factors(num:int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count
print(count_factors(n))