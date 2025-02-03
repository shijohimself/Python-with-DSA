n = input("Enter string = ")
def reverse_str(string):
    result = ""
    length = len(string)
    for index in range(length-1,-1,-1):
        result += string[index]
    return result


print(reverse_str(n))
