# Task Nr.2 : Write a User class that has a password property. 
# The password property should be a computed property that checks whether the password is strong enough. 
# A password is considered strong if it has at least 8 characters, contains at least one uppercase letter,
# one lowercase letter, and one number.

import re

class User:
    def __init__(self, password: str):
        self._password = None
        self.password = password

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, new_password: str) -> None:
        if self.is_strong_password(new_password):
            self._password = new_password
        else:
            raise ValueError("Password is not strong enough.")

    @staticmethod
    def is_strong_password(password: str) -> bool:
        if len(password) < 8:
            return False

        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)

        return has_uppercase and has_lowercase and has_digit


user = User("Str0")  # A strong password will be accepted
print(user.password)

try:
    user.password = "weakpass"  # A weak password will raise a ValueError
except ValueError as e:
    print(e)
