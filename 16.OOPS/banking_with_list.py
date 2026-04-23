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

banks = []

x = Bank()
banks.append(x)
print(banks)

y = Bank()
banks.append(y)
print(banks)

banks[0].show_balance()
banks[1].deposit()
banks[1].show_balance()