class BankAccount:
    IBAN: str
    balance: int = 0
    currency: str
    isOpen: bool

    def __init__(self, IBAN, currency = "CHF"):
        self.IBAN = IBAN
        self.currency = currency
        self.isOpen = True

    def deposit(self, amount):
        if not self.isOpen:
            return False

        if amount < 0:
            return False
        
        self.balance += amount
        if self.balance > 100000:
            return False

        return True

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if not self.isOpen:
            return False

        if amount < 0:
            return False
        
        self.balance -= amount
        if self.balance < 0:
            return False

        return True

    def open(self):
        self.isOpen = True

    def close(self):
        self.isOpen = False

account = BankAccount("12345", "CHF")