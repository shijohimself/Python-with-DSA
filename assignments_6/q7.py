n = int(input("enetr your value = "))
def harmonic_series(num):
    i = 1
    count = 0
    while i <= num:
        count = count + 1/i
        i += 1
    return count
x = harmonic_series(n)
print(f"{x:.2f}")
