import logging
from typing import Union

logging.basicConfig(filename='country.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

class Country:
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()

    def check_if_big(self) -> bool:
        if self.population > 250000000 or self.area > 3000000:
            return True
        return False

    def compare_pd(self, other_country: 'Country') -> str:
        self_pd = self.population / self.area
        other_pd = other_country.population / other_country.area
        if self_pd > other_pd:
            return f"{self.name} has a larger population density than {other_country.name}"
        elif self_pd < other_pd:
            return f"{self.name} has a smaller population density than {other_country.name}"
        else:
            return f"{self.name} has the same population density as {other_country.name}"

if __name__ == '__main__':
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)

    logging.info(f"{australia.name} is_big: {australia.is_big}")
    logging.info(f"{andorra.name} is_big: {andorra.is_big}")
    logging.info(andorra.compare_pd(australia))
