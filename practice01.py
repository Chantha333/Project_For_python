class BankAccount:
    def __init__(self,balance,name,secret):
        self.__balance=balance
        self.name=name
        self.__secret=secret

    def withdraw(self,amount,secret):
        print(f"{self.name} withdraw is success!")
        if secret==self.__secret:
            remain=self.__balance - amount
            if remain<0:
                print("you don't withdraw!")
            else:
                self.__balance=remain
                print(" Withdraw is successfuly!") 
                print(f"You remaining balance is {self.__balance}")
        else:
            print("invalin secret. please try again!")

    def deposit(self,amount,secret):
        if secret==self.__secret:
            if amount<=0:
                print("Invalid Amount!")
            else:
                self.__balance+=amount
                print(f"{self.name} deposit successfully!")
                print(f"New balacne : {self.__balance}")
        else:
            print("Invalid Secret!!")            

    def payment(self,service_type,amount,secret):
        if secret==self.__secret:
            if self.__balance>=amount:
                self.__balance-=amount
                print(f"Paid {amount} for {service_type} ")
                print(f"Remaining balance: {self.__balance}")
            else:
                print("Not enought balance!")
        else:
            print("Invalid secret!!")        

    def transfer(self,to_name,amount,secret):            
        if secret==self.__secret:
            if self.__balance>=amount:
                self.__balance-=amount
                to_name.__balance+=amount
                print(f"Transfer{amount} for {to_name.name} succeessfully!!")
                print(f"Remaining balance : {self.__balance}")
            else:
                print("Not enought balacne!!")    
        else:
            print("Invalid secret!!")
        
    def check(self,secret):
        if secret == self.__secret:
            print(f"{self.name} remaining balance is {self.__balance}") 
        else:
            print(" I don't know you !")
user1=BankAccount(balance=2000,name="Dara",secret="111")     
user2=BankAccount(balance=5000,name="Bora",secret="222")
print("====== WELCOME TO ATM ======")

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Payment")
    print("5. Transfer")
    print("6. Exit")

    choice = input("Choose option (1-6): ")
    secret = input("Enter your secret: ")

    if choice == "1":
        user1.check(secret)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        user1.deposit(amount, secret)

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        user1.withdraw(amount, secret)

    elif choice == "4":
        service = input("Enter service name (e.g., Electricity, Water): ")
        amount = float(input("Enter payment amount: "))
        user1.payment(service, amount, secret)

    elif choice == "5":
        print(f"Transfer to {user2.name}")
        amount = float(input("Enter transfer amount: "))
        user1.transfer(user2, amount, secret)

    elif choice == "6":
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")