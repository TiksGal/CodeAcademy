# Create a class which takes temperature measurements in Kelvins and add static methods 
# to transform those to Celsius and Fahrenheit units. Use OOP abstraction.

class Temperature():
    
    @staticmethod
    def to_celsius(kelvin: float) -> float:
        return round(kelvin - 273.15, 2)
    
    @staticmethod
    def to_fahrenheit(kelvin: float) -> float:
        return round(kelvin * 9/5 - 459.67, 2)
    
    
print(f"Celsius: {Temperature.to_celsius(100)}")
# output: -173.14999999999998
print(f"Fahrenheit: {Temperature.to_fahrenheit(100)}")
# output: -279.67

        