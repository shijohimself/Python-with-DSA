a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral Traingle!!")
    elif a == b or b == c or a == c :
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Traingle!")
 