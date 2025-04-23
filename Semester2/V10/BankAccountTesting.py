import unittest
from BankApp import BankApplication
import time

class BankAccountTesting(unittest.TestCase):
    app: BankApplication

    def setUp(self) -> None:
        self.app = BankApplication()
        self.savingAccount = self.app.open_account("saving", "CH1234567890123456789", 25, "CHF")
        self.youthAccount = self.app.open_account("youth", "CH9876543210987654321", 20, "USD")
        self.app.switch_account("CH1234567890123456789")
        self.app.deposit(1000)
        self.app.switch_account("CH9876543210987654321")
        self.app.deposit(2000)
    
    def test_switch_account(self):
        self.app.switch_account("CH9876543210987654321")
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 2000)
        self.assertEqual(currency, "USD")
    
    def test_deposit(self):
        self.app.switch_account("CH1234567890123456789")
        self.app.deposit(500)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 1500)
        self.assertEqual(currency, "CHF")
    
    def test_withdraw(self):
        self.app.switch_account("CH1234567890123456789")
        self.app.withdraw(500)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 500)
        self.assertEqual(currency, "CHF")

    def test_negative(self):
        self.app.switch_account("CH1234567890123456789")
        self.app.withdraw(-500)#should not be allowed
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 1000)

        self.app.switch_account("CH9876543210987654321")
        self.app.deposit(-500)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 2000)

    def test_overdraw(self):
        self.app.switch_account("CH9876543210987654321")
        self.app.withdraw(3000)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 2000)
        
    def test_overdeposit(self):
        self.app.switch_account("CH1234567890123456789")
        self.app.deposit(200000)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 1000)

    def test_interest(self):
        time.sleep(10)  # Simulate 10 seconds passing
        self.app.switch_account("CH1234567890123456789")
        balance, currency = self.app.getBalance()
        self.assertAlmostEqual(balance, 1001)
        self.assertEqual(currency, "CHF")

        self.app.switch_account("CH9876543210987654321")
        balance, currency = self.app.getBalance()
        self.assertAlmostEqual(balance, 2040)
        self.assertEqual(currency, "USD")

    def test_invalid_account_type(self):
        self.app.open_account("invalid", "CH1111111111111111111")
        self.assertNotIn("CH1111111111111111111", self.app.accounts)

    def test_invalid_age(self):
        self.app.open_account("youth", "CH2222222222222222222", 30)
        self.assertNotIn("CH2222222222222222222", self.app.accounts)

    def test_max_withdraw(self):
        self.app.switch_account("CH9876543210987654321")
        self.app.deposit(2000)
        self.app.withdraw(2000)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 2000)
        self.app.withdraw(1)
        balance, currency = self.app.getBalance()
        self.assertEqual(balance, 2000)


if __name__ == "__main__":
    unittest.main()