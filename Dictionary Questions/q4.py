n = int(input("Enter the number of subjects = "))
mydict = {

}

for i in range(n):
    subject_name = input("Enter subject name = ")
    marks = int(input("Enter marks = "))
    mydict[subject_name] = marks

print(mydict)
