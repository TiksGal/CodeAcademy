# Write a Temperature class that has a celsius property and a fahrenheit property.
# The celsius property stores the temperature in Celsius, and the fahrenheit property stores the temperature in Fahrenheit.
# The fahrenheit property should be a computed property that converts the Celsius temperature to Fahrenheit.

class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32
    
temp = Temperature(100)
print(f"Celsius: {temp.celsius}")  # Output: 100
print(f"Fahrenheit: {temp.fahrenheit}")  # Output: 212.0