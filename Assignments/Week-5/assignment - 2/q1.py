n = int(input("Enter number of subjects: "))

my_dict = {}
for i in range(n):
    sub = input("enter subject name = ")
    marks = int(input("enter marks = "))
    my_dict[sub] = marks
print(my_dict)

