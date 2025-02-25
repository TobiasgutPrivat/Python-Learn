class BankAccount:
    IBAN: str
    balance: int
    currency: str

    def __init__(self, IBAN, currency = "CHF"):
        self.IBAN = IBAN
        self.balance = 0
        self.currency = currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        
        self.balance += amount
        if self.balance > 100000:
            raise ValueError

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        
        self.balance -= amount
        if self.balance < 0:
            raise ValueError