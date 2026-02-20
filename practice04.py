
class BankAccount:
    def __init__(self, balance, name, secret):
        self._balance = balance
        self.name = name
        self._secret = secret


    def verify(self, secret):
        return self._secret == secret

    def check_balance(self):
        print(f"Your balance is ${self._balance}")


    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Invalid amount!")
        else:
            self._balance += amount
            print("Deposit successful!")
            print(f"New balance: ${self._balance}")

  
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > self._balance:
            print("Not enough balance!")
        else:
            self._balance -= amount
            print("Withdraw successful!")
            print(f"Remaining balance: ${self._balance}")

   
    def payment(self):
        service = input("Enter service name: ")
        amount = float(input("Enter payment amount: $"))
        if amount > self._balance:
            print("Not enough balance!")
        else:
            self._balance -= amount
            print(f"Paid ${amount} for {service}")
            print(f"Remaining balance: ${self._balance}")

    def transfer(self, account_list):
        receiver_name = input("Enter receiver name: ")
        amount = float(input("Enter transfer amount: $"))

        for acc in account_list:
            if acc.name == receiver_name:
                if amount > self._balance:
                    print("Not enough balance!")
                    return
                self._balance -= amount
                acc._balance += amount
                print("Transfer successful!")
                print(f"Remaining balance: ${self._balance}")
                return

        print("Receiver not found!")



class SavingAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.02
        self._balance += interest
        print(f"Interest added: ${interest}")
        print(f"New balance: ${self._balance}")



class StudentBankAccount(BankAccount):
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 500:
            print("Maximum withdrawal is $500!")
        elif amount > self._balance:
            print("Not enough balance!")
        else:
            self._balance -= amount
            print("Withdraw successful!")
            print(f"Remaining balance: ${self._balance}")



class PremiumSaving(SavingAccount):
    def deposit(self):
        amount = float(input("Enter amount to deposit: $"))
        interest = amount * 0.02
        self._balance += amount + interest
        print(f"Deposit successful with 2% interest (${interest})")
        print(f"New balance: ${self._balance}")


class BusinessAccount(BankAccount):
    def take_loan(self):
        amount = float(input("Enter loan amount: $"))
        interest_rate = 0.7
        total_payment = amount + (amount * interest_rate / 100)

        print("Loan approved!")
        print(f"Interest rate: {interest_rate}%")
        print(f"Total payment required: ${total_payment}")

        self._balance += amount
        print(f"New balance: ${self._balance}")


user1 = BankAccount(4000, "Dara", "111")
user2 = BankAccount(5000, "Bora", "222")
user3 = SavingAccount(3000, "Long", "333")
user4 = StudentBankAccount(2000, "Coca", "444")
user5 = PremiumSaving(6000, "Heng", "555")
user6 = BusinessAccount(19000, "Tha", "666")

account_list = [user1, user2, user3, user4, user5, user6]



print("====== WELCOME TO ATM ======")

while True:
    print("\n1. Login")
    print("2. Exit")
    main_choice = input("Choose option: ")

    if main_choice == "2":
        print("Thank you! Goodbye.")
        break

    name = input("Enter your name: ")
    secret = input("Enter your secret: ")

    acc_login = None
    for acc in account_list:
        if acc.name == name and acc.verify(secret):
            acc_login = acc
            break

    if acc_login is None:
        print("Incorrect name or secret!")
        continue

    print(f"\nWelcome {acc_login.name}!")

    while True:
        print("\n1.Check Balance")
        print("2.Withdraw")
        print("3.Deposit")
        print("4.Payment")
        print("5.Transfer")
        print("6.Logout")

        if isinstance(acc_login, SavingAccount):
            print("7.Add Interest")

        if isinstance(acc_login, BusinessAccount):
            print("8.Take Loan")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_login.check_balance()
        elif choice == "2":
            acc_login.withdraw()
        elif choice == "3":
            acc_login.deposit()
        elif choice == "4":
            acc_login.payment()
        elif choice == "5":
            acc_login.transfer(account_list)
        elif choice == "6":
            print("Logging out...")
            break
        elif choice == "7" and isinstance(acc_login, SavingAccount):
            acc_login.add_interest()
        elif choice == "8" and isinstance(acc_login, BusinessAccount):
            acc_login.take_loan()
        else:
            print("Invalid choice!")
