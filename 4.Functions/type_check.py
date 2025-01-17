a = 55

def type_check(a):
    # if type(a) == int:
    #     return True
    # return False

    if isinstance(a,int): # isinstance returns boolean value!
        return True
    return False

print(type_check(a))