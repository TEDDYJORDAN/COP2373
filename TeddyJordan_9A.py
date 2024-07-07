class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%")

def test_bank_acct():
    # Create an account
    acct = BankAcct("Teddy Jordan", "987654321", 10000.00, 4.0)

    # Display initial account information
    print(acct)

    # Test deposit
    acct.deposit(500.00)
    print("\nAfter depositing $500.00:")
    print(acct)

    # Test withdrawal
    acct.withdraw(200.00)
    print("\nAfter withdrawing $200.00:")
    print(acct)

    # Test interest calculation for 30 days
    interest = acct.calculate_interest(30)
    print(f"\nInterest for 30 days: ${interest:.2f}")

    # Adjust interest rate
    acct.adjust_interest_rate(4.0)
    print("\nAfter adjusting interest rate to 4.0%:")
    print(acct)

    # Test balance method
    balance = acct.get_balance()
    print(f"\nCurrent balance: ${balance:.2f}")

if __name__ == "__main__":
    test_bank_acct()