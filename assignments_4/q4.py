# curzon number:
number = int(input("Enter num: "))
def is_curzon(num):
    curzon = 1 + (2 ** num)
    if curzon % (1 + (2 * num)) == 0:
        return True
    return False

print(is_curzon(number))

