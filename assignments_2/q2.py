total_class = int(input("Total classes held: "))
class_attended = int(input("Total number of classes attended: "))

percentage_of_class_attended = (class_attended/100) * total_class
print(percentage_of_class_attended)

if percentage_of_class_attended < 75:
    print("You are not allowed to sit in exam!")
else:
    print("Congrats! You are eligible!!")