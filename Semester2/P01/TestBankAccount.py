import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("12345", "CHF")

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)
        
        with self.assertRaises(ValueError):
            self.account.deposit(100000)

        with self.assertRaises(ValueError):
            self.account.deposit(-1)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

        with self.assertRaises(ValueError):
            self.account.withdraw(100)

        with self.assertRaises(ValueError):
            self.account.withdraw(-1)

if __name__ == '__main__':
    unittest.main()