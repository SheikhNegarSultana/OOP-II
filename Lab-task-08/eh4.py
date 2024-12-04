class LowBalanceError(Exception):
    pass

class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def withdraw_funds(self, amount_to_withdraw):
        if self.balance < amount_to_withdraw:
            raise LowBalanceError("Insufficient funds for this withdrawal.")
        self.balance -= amount_to_withdraw
        print(f"Withdrawal successful. Remaining balance: {self.balance}")

try:
    user_account = Account(5000)
    user_account.withdraw_funds(10000)
except LowBalanceError as error:
    print(f"Error: {error}")
except Exception:
    print("An unexpected error occurred.")
