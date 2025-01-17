a = 55

def type_check(num):
    # if type(a) == int:
    #     return True
    # return False

    if isinstance(num,int): # isinstance returns boolean value!
        return True
    return False

print(type_check(a))