import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Set up a new BankAccount for every test."""
        self.account = BankAccount()

    #case1
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), "Your total balance : " + str(0))
        
    #case2
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), "Your total balance : " + str(100))
    #case3
    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), "Your total balance : " + str(50))
    #case4
    def test_negative_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-50)
        self.assertEqual(str(context.exception), "Deposit amount should be positive")
    #case5
    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-50)
        self.assertEqual(str(context.exception), "Amount should be positive!")
    #case6
    def test_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(50)
        self.assertEqual(str(context.exception), "Balance is insufficient!")
if __name__ == "__main__":
    unittest.main()


# Install pytest
# pip3 install pytest

# How to run unit test
# python3 -m unittest test_bank_account.py

# How to check coverage 
# pip3 install coverage

# check coverage 
# coverage run -m unittest test_bank_account.py

#In Terminal
# coverage report

# In HTML
# coverage html

