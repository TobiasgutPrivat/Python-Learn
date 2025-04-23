from SavingAccount import SavingAccount
from YouthAccount import YouthAccount
from BankAccount import BankAccount

class BankApplication:
    accounts: dict[str, BankAccount] = {}
    currentAccount: BankAccount | None = None

    def open_account(self, type: str, IBAN: str, age: int | None = None, currency: str = "CHF"):
        if type == "saving":
            self.accounts[IBAN] = SavingAccount(IBAN, currency)
            self.accounts[IBAN].open()
        elif type == "youth":
            if age is None or age > 25:
                print("Youth account can only be opened for people 25 or younger.")
                return
            self.accounts[IBAN] = YouthAccount(IBAN, currency)
            self.accounts[IBAN].open(age)
        else:
            print("Invalid account type.")
        
        print(f"Account {IBAN} opened.")

    def switch_account(self, acc_id):
        if acc_id in self.accounts:
            self.currentAccount = self.accounts[acc_id]
            print(f"Switched to account {acc_id}")
        else:
            print("Account not found.")

    def deposit(self, amount):
        if self.currentAccount:
            if not self.currentAccount.deposit(amount):
                print("Deposit failed.")
        else:
            print("No account selected.")

    def withdraw(self, amount):
        if self.currentAccount:
            if not self.currentAccount.withdraw(amount):
                print("Withdraw failed.")
        else:
            print("No account selected.")

    def getBalance(self) -> tuple[int, str]:
        if self.currentAccount:
            balance, currency = self.currentAccount.getBalance()
            return balance, currency
        else:
            print("No account selected.")
            return 0, ""
        
    def check_balance(self):
        if self.currentAccount:
            balance, currency = self.currentAccount.getBalance()
            print(f"Balance: {balance} {currency}")
        else:
            print("No account selected.")
