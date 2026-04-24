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

def check_account_exists(acc_no:int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None

while True:
    print("""
1. Create account
2. Show all bank details
3. Deposit amount
4. Withdraw amount
5. Transfer amount
6. Exit
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
        from_account_no = int(input("enter account number from which you want to transfer = "))
        to_account_no = int(input("enter account number to which you want to transfer = "))
        if len(banks) == 0:
            print("No accounts found")
        else:
            from_account_obj = check_account_exists(from_account_no)
            to_account_obj = check_account_exists(to_account_no)
            if from_account_obj != None and to_account_no != None:
                transfer_amount = int(input("enter transfer amount = "))
                if from_account_obj.balance < transfer_amount:
                    print("insuffiencent balance")
                else:
                    from_account_obj.balance -= transfer_amount
                    to_account_obj.balance += transfer_amount
            else:
                print("Account does not exists!")
    elif choice == 6:
        break
    else:
        print("invalid choice")
