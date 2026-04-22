class Student:
    roll_number = 0
    name = ""
    age = 0
    gender = ""
    address = ""

    # methods
    def info(self):
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
    
    def set_info(self):
        self.name = input("enter name = ")
        self.address = input("enter address = ")
        self.age = int(input("enter age = "))
        self.gender = input("enter gender = ")


s1 = Student()
s2 = Student()
s3 = Student()
s1.name = "Shijo"
s1.roll_number = 10
print(s1.name)
print(s1.roll_number)
s1.info()
print("===============")
print(s2.name)
print(s2.roll_number)
s3.set_info()
s3.info()