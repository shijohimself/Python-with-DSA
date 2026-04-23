from random import randint
class Bank:
    def __init__(self):
        self.account = randint(100000,999999)
        self.full_name = input("enter name = ")
        self.balance = 0
        self.phone_number = int(input("enter phone number = "))

    def show_balance(self):
        print(f"current balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficent balance!")
        else:
            self.balance -= amount
    
    def deposit(self) -> None:
        amount = int(input("enter amount = "))
        self.balance += amount

b1 = Bank()
b1.show_balance()
b1.deposit()
b1.show_balance()
b1.withdraw()
b1.show_balance()
