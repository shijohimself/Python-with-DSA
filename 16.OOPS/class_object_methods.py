class Student:

    def __init__(self):
        self.name = input("enter name = ")
        self.address = input("enter address = ")
        self.age = int(input("enter age = "))
        self.gender = input("enter gender = ")
        
    # methods
    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
       
s1 = Student()
s2 = Student()
s3 = Student()
s1.name = "Shijo"
print(s1.name)
s1.info()
print("===============")
print(s2.name)
s3.info()
