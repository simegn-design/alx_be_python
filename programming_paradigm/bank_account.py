class BankAccount:
    """A simple bank account class with deposit/withdraw functionality."""
    
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add amount to balance."""
        self.account_balance += amount
    
    def withdraw(self, amount):
        """Deduct amount if sufficient funds exist."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Print formatted balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
