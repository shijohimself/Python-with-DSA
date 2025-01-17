
def product(n1,n2):
    pro = n1 * n2
    return pro

def check_div_by_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

x = product(10,20)
print(x)

y = product(30,40)
print(y)
z = check_div_by_5(y)
print(z)