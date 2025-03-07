from BankApp import BankApplication
from TaxReport import TaxReport
import time

app = BankApplication()
app.open_account("saving", "S123")
app.open_account("youth", "Y456", age=22)

app.switch_account("S123")
app.deposit(5000)
app.withdraw(200)
app.check_balance()

time.sleep(10)  # Simulate one month
app.check_balance()

TaxReport.generate(app)