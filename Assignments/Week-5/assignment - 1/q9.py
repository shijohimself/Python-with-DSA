#count digits


my_str = "ashdhih678643676579"

def count_digits(string):
    count = 0
    for ch in string:
        asc = ord(ch)
        if asc >=48 and asc <= 57:
            count += 1
    return count
print(count_digits(my_str))
