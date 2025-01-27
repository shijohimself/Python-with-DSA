"""
ask a num from user = 6

n1
n2
n3
n4
n5
n6

[n1,n2,n3,n4,n5,n6]
"""
from typing import List


def create_list(length:int) -> List[int]:
    L = []
    for i in range(length):
        num = int(input(f"Enter num {i+1} = "))
        L.append(num)
    return L

lst = create_list(6)
print(lst)
