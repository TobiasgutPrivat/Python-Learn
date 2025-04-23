from BankApp import BankApplication
from ExchangeRate import get_exchange_rate

class TaxReport:
    @staticmethod
    def generate(bankApp: BankApplication):
        print("\nTax Report")
        print("===========")
        total = 0
        for acc_id, account in bankApp.accounts.items():
            balance, currency = account.getBalance()
            chf = balance / get_exchange_rate(currency)
            print(f"{acc_id}: {chf} CHF")
            total += chf
        print(f"Total Wealth: {total} CHF")