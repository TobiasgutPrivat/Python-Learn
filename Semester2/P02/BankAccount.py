from datetime import datetime

class BankAccount:
    IBAN: str
    balance: int = 0
    currency: str
    isOpen: bool = False
    startTime: datetime = datetime.now() # 10sec = 1month
    monthlyInterestRate: float = 1
    accountedMonths: int = 0
    withdrawThisMonth: int = 0
    allowNegative: bool = False

    def __init__(self, IBAN, currency = "CHF"):
        self.IBAN = IBAN
        self.currency = currency

    def getBalance(self):
        return self.balance

    def deposit(self, amount) -> bool:
        if not self.isOpen:
            return False

        if amount < 0:
            return False
        
        if self.balance + amount > 100000:
            return False
        
        self.balance += amount

        return True
    
    def withdraw(self, amount) -> bool:
        if not self.isOpen:
            return False

        if amount < 0:
            return False
        
        if (not self.allowNegative) and (self.balance - amount < 0):
            return False
        
        self.balance -= amount

        self.withdrawThisMonth += amount

        return True
    
    def __getattribute__(self, name):
        if name in ["withdraw", "deposit", "getBalance"]:
            self.updateMonthInfo()
        return super().__getattribute__(name)

    def updateMonthInfo(self):
        time = datetime.now() - self.startTime
        months = (time.seconds // 10) - self.accountedMonths
        self.accountedMonths += months
        for i in range(months):
            self.balance *= self.monthlyInterestRate
        if months > 0:
            self.withdrawThisMonth = 0

    def open(self):
        self.isOpen = True

    def close(self):
        self.isOpen = False