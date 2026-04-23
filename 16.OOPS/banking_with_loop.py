from random import randint
class Bank:
    def __init__(self):
        self.account = randint(100000,999999)
        self.full_name = input("enter name = ")
        self.balance = 0
        self.phone_number = int(input("enter phone number = "))

    def show_balance(self):
        print(f"current balance = {self.balance}")

    def show_info(self):
        print(f"account number = {self.account}")
        print(f"full name  = {self.full_name}")
        print(f"current balance = {self.balance}\n")

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

while True:
    print("""
1. Create account
2. Show all bank details
3. Deposit amount
4. Withdraw amount
5. Exit
""")
    choice = int(input("enter your choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts created")
        else:
            for accounts in banks:
                accounts.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No accounts have been created")
        else:
            acc_no = int(input("enter account number = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
    elif choice == 4:
        if len(banks) == 0:
            print("No account present!")
        else:
            acc_no = int(input("Enter account num = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        break
    else:
        print("invalid choice")
