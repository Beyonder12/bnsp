class BankAccount:
    def __init__(self, balance = 0):
        print("Your initial balance : " + str(balance))
        self.balance = balance

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
    
fajriAccount = BankAccount()
fajriAccount.deposit(10)
print(fajriAccount.get_balance())