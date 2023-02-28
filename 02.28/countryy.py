class Country:
    def __init__(self, name: str, population: int, area: int) -> bool:
        self.name = name
        self.population = population
        self.area = area
        self.is_big = False
        if self.population > 250_000_000 or self.area > 3_000_000:
            self.is_big = True
    
    def compare_pd(self, other_country: str) -> str:
        if self.population / self.area > other_country.population / other_country.area:
            return f"{self.name} has a larger population density than {other_country.name}"
        else:
            return f"{self.name} has a smaller population density than {other_country.name}"

# Create two country objects
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

# Access the instance attributes and methods
print(australia.is_big)
print(andorra.is_big)
print(andorra.compare_pd(australia))
