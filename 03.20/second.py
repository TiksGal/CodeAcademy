from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, currency: str, value: float):
        self.currency = currency
        self.value = value
        
    def get_value(self) -> float:
        return self.value

    def get_currency(self) -> str:
        return self.currency
    
    @abstractmethod
    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> None:
        pass

class Cash(Money):
    def __init__(self, currency: str, value: float, denomination: int):
        super().__init__(currency, value)
        self.denomination = denomination

    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> None:
        self.value = round(self.value * self.currency * target_currency,2)
        self.currency = target_currency

class Card(Money):
    def __init__(self, currency: str, value: float, credit_limit: float):
        super().__init__(currency, value)
        self.credit_limit = credit_limit

    def convert_to_currency(self, target_currency: str, conversion_rate: float) -> None:
        self.value = round(min(self.value, self.credit_limit) * self.currency * target_currency,2)
        self.currency = target_currency