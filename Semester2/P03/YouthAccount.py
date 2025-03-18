from BankAccount import BankAccount

class YouthAccount(BankAccount):
    monthlyInterestRate: float = 1.02

    def withdraw(self, amount) -> bool:
        if self.withdrawThisMonth + amount > 2000:
            return False

        return super().withdraw(amount)
    
    def open(self, age):
        if age <= 25:
            super().open()