def marks(s1:int,s2:int,s3:int,s4:int,s5:int):
    total = s1 + s2 + s3 + s4 + s5
    if total >= 33*5:
        return True
    return False

print(marks(10,20,30,30,50))