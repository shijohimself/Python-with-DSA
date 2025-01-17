def avg(n1:int,n2:int, n3:int, n4:int,n5:int) -> float:
    total = n1 + n2 + n3 + n4 + n5
    return total / 4

def add(num1:int,num2:int) -> None:
    addition = num1+ num2
    print(addition)

print(avg(10,20,40,50,60))
add(20,30)