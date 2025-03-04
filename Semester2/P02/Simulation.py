import time
from SavingAccount import SavingAccount
from YouthAccount import YouthAccount

# Simulation example for both account types
def simulate():
    # Creating a Saving Account
    saving_account = SavingAccount("CH1234567890")
    saving_account.open()
    
    # Create a Youth Account (age 23)
    youth_account = YouthAccount("CH0987654321")
    youth_account.open(age=23)

    # Deposit some amount
    saving_account.deposit(1000)
    youth_account.deposit(500)

    print(f"Saving Account Balance after deposit: {saving_account.getBalance()} CHF")
    print(f"Youth Account Balance after deposit: {youth_account.getBalance()} CHF")

    # Wait for 30 seconds to simulate 3 months
    time.sleep(30)
    
    # Check balances after simulated interest
    print(f"Saving Account Balance after 3 months: {saving_account.getBalance()} CHF")
    print(f"Youth Account Balance after 3 months: {youth_account.getBalance()} CHF")

    # Perform a withdrawal from Saving Account with penalty
    print("Withdrawing from Saving Account (penalty case):")
    saving_account.withdraw(1200)  # Withdrawal amount greater than the balance
    print(f"Saving Account Balance after withdrawal with penalty: {saving_account.getBalance()} CHF")
    
    # Perform a withdrawal from Youth Account (limit exceeded)
    print("Withdrawing from Youth Account (limit exceeded):")
    result = youth_account.withdraw(2500)  # Exceeds monthly withdrawal limit
    print(f"Withdrawal successful: {result}. Balance: {youth_account.getBalance()} CHF")

    # Perform a withdrawal from Youth Account (within limit)
    print("Withdrawing from Youth Account (within limit):")
    youth_account.withdraw(1500)  # Withdraw within the limit
    print(f"Youth Account Balance after withdrawal: {youth_account.getBalance()} CHF")

# Run the simulation
if __name__ == "__main__":
    simulate()
