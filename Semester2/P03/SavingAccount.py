from BankAccount import BankAccount

class SavingAccount(BankAccount):
    monthlyInterestRate: float = 1.001
    allowNegative: bool = True
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return super().withdraw(amount * 1.02) # 2% penalty
        else:
            return super().withdraw(amount)
        