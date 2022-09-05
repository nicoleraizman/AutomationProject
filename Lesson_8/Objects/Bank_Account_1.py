class Bank_Account_1:
    # account_number, name, balance, transactions

    def __init__(self, number: int, name: str):
        """Constructor that initialize the attributes of the object"""
        self.number = 0
        self.name = ""
        self.balance = 0
        self.transactions = []

    def bank_statement(self):
        print(f"Account number: {self.number} Name: {self.name} Balance: {self.balance}")
    def deposit(self):
        self.
    def withdraw(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount

my_account = Bank_Account_1()
my_account.