for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end = " ")
    for k in range((5-i)+1,6):
        print(k , end = " ")
    print()