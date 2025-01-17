"""
make a func named marks, it should take 5 int as a parameter
print the total
print percentage
"""

def marks(n1:int,n2:int,n3:int,n4:int,n5:int):
    total = n1 + n2 + n3 + n4 + n5
    print(f"Your total is = {total}")
    percentage = (total/ 500) * 100
    print(percentage)

marks(20,40,70,92,98)