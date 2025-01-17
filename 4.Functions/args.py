def add(n1,n2, *args):
    print(f"n1 = {n1}")
    print(f"n2 = {n2}")
    print(f"remaining = {args}")
# args by default tuple
add(10,20,50,60,70,50,80,30)