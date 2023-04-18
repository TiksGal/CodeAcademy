from typing import Union

class BankAccount:
    def __init__(self, account_number: str, balance: float) -> None:
        self.account_number = account_number
        self.balance = balance

    def __bool__(self) -> bool:
        return self.balance > 0

    def __repr__(self) -> str:
        return f"BankAccount('{self.account_number}', {self.balance})"

    def __str__(self) -> str:
        return f"BankAccount {self.account_number} with balance: {self.balance}"

    def __eq__(self, other: 'BankAccount') -> bool:
        return self.account_number == other.account_number and self.balance == other.balance

    def __add__(self, other: 'BankAccount') -> "BankAccount":
        if self.account_number != other.account_number:
            raise ValueError("Cannot add balances of different accounts")
        return BankAccount(self.account_number, self.balance + other.balance)
    
    
account1 = BankAccount("12345", 1000)
account2 = BankAccount("12345", 500)
account3 = BankAccount("67890", 1000)

# Spausdiname sąskaitas
print(account1)  # Output: BankAccount 12345 with balance: 1000
print(repr(account2))  # Output: BankAccount('12345', 500)

# Patikriname ar sąskaitos balansas yra didesnis už 0
print(bool(account1))  # Output: True

# Sudedame sąskaitų balansus
combined_account = account1 + account2
print(combined_account)  # Output: BankAccount 12345 with balance: 1500

# Patikriname ar sąskaitų balansai lygūs
print(account1 == account2)  # Output: False
print(account1 == account3)  # Output: False

