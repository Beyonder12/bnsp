class BankAccount:

    # Attribute/Properties/Field
    balanceAtt = 0

    # Constructor/Initialization
    def __init__(self, balance = balanceAtt):
        print("Your initial balance : " + str(balance))
        self.balance = balance

    # Method/Function/Behavior
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be positive")
        self.balance += amount
        print("Action : Deposit -> Your balance is added: " + str(amount))
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount should be positive!")
        if amount > self.balance:
            raise ValueError("Balance is insufficient!")
        self.balance -= amount
        print("Action : Withdraw -> Your balance is withdrawn: " + str(amount))

    def get_balance(self):
        return "Your total balance : " + str(self.balance)
    
fajriAccount = BankAccount(100)
fajriAccount.deposit(10)
fajriAccount.withdraw(60)
print(fajriAccount.get_balance())