class Bank_Account:
    # account_number, name, balance, transactions

    def __init__(self,number:int,name:str,balance=0):
        """Constructor that initialize the attributes of the object"""
        self.number = number
        self.name = name
        self.balance = balance
        self.credit_limit=-500
        self.transactions = []

    def bank_statement(self):
        print(f"Account number: {self.number} Name: {self.name} Balance: {self.balance} {self.transactions}")

    def deposit(self,amount:int):
        self.balance+=amount
        self.transactions.append(amount)
        self.bank_statement()

    def withdraw(self, amount:int):
        if self.balance-amount >= self.credit_limit:
            self.balance-=amount
            self.transactions(-amount)
        else:
            print("Not enough money in the account")
        self.bank_statement()

    def __str__(self):
        """Return a string with all the details we want to print"""
        print("I am __str__")
        return f"Account number: {self.number} Name: {self.name} Balance: {self.balance} {self.transactions}"
# create an object my_account of type(class) Bank_Account
# print(type(my_account))

number=int(input("Enter account number: "))
name=input("Enter name: ")

my_account = Bank_Account(number, name)
my_account.balance=400


amount=int(input("Enter amount to withdraw: "))
my_account.withdraw(amount)

