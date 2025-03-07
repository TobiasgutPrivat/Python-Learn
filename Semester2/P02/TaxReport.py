from BankApp import BankApplication

class TaxReport:
    @staticmethod
    def generate(bankApp: BankApplication):
        print("\nTax Report")
        print("===========")
        total = 0
        for acc_id, account in bankApp.accounts.items():
            print(f"{acc_id}: {account.getBalance()} {account.currency}")
            total += account.getBalance()
        print(f"Total Wealth: {total} {account.currency}")