import logging
from typing import Union

# Set up logging to write to a file
logging.basicConfig(filename='country.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

class Country:
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area
        self.is_big = False
        if self.population > 250_000_000 or self.area > 3_000_000:
            self.is_big = True
    
    def compare_pd(self, other_country: "Country") -> str:
        if not isinstance(other_country, Country):
            logging.error("Invalid comparison object type")
            raise TypeError("Invalid comparison object type")
        if other_country.area == 0:
            logging.warning("Comparison country has area of 0")
            return f"{self.name} has an infinite population density compared to {other_country.name}"
        elif self.area == 0:
            logging.warning("This country has area of 0")
            return f"{self.name} has a population density of 0 compared to {other_country.name}"
        elif self.population / self.area > other_country.population / other_country.area:
            return f"{self.name} has a larger population density than {other_country.name}"
        else:
            return f"{self.name} has a smaller population density than {other_country.name}"

# Example usage and error handling
try:
    # Create two country objects
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)

    # Access the instance attributes and methods
    logging.info("Country objects created successfully")
    print(australia.is_big)  # True
    print(andorra.is_big)  # False
    print(andorra.compare_pd(australia))  # Andorra has a larger population density than Australia
    # The following line will raise a TypeError and be caught by the try-except block
    # print(andorra.compare_pd("invalid input"))
except Exception as e:
    logging.exception(f"An error occurred: {e}")
    
if __name__ == '__main__':
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)

    logging.info(f"{australia.name} is_big: {australia.is_big}")
    logging.info(f"{andorra.name} is_big: {andorra.is_big}")
    logging.info(andorra.compare_pd(australia))

