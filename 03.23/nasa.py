# Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and Space Shuttle classes.
# Create a simple calculator with:

# Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).
# Through the main class you should be able to calculate the mission cost which includes:
#     fuel cost (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))),
#     average personals expenditures ( ppl x base_salary ).
# Prepare the final report in the file document and on screen with a method get_full_report 
# with all gathered and calculated data.
# import time

# class Carrier():
#     """Shuttle cost currency is USD
#     Shuttle weight is in kg
#     Year built should be in this format: YYYY"""
#     def __init__(self, cost: float, year_built: int, weight: float) -> None:
#         self._cost: float = cost
#         self._year_built: int = year_built
#         self._weight: float = weight
        
#     def get_age(self) -> int:
#         current_timestamp = time.time()
#         current_year = time.gmtime(current_timestamp).tm_year
#         return current_year - self._year_built
    
#     def get_cost(self) -> float:
#         return self._cost
    
#     def get_weight(self) -> float:
#         return self._weight
    
#     def get_year_built(self) -> int:
#         return self._year_built


# class SpaceShuttle(Carrier):
#     def __init__(self, cost: float, year_built: int, weight: float, orbit_height: float, burn_rate: float) -> None:
#         super().__init__(cost, year_built, weight)
#         self._orbit_height = orbit_height
#         self._burn_rate = burn_rate
#         self._fuel_cost = 1.4
#         self._base_salary = 40000
#         self._ppl = 7
    
#     def get_orbit_height(self) -> float:
#         return self._orbit_height
    
#     def get_burn_rate(self) -> float:
#         return self._burn_rate
    
#     def get_fuel_cost(self) -> float:
#         return self._fuel_cost
    
#     def get_base_salary(self) -> float:
#         return self._base_salary
    
#     def get_ppl(self) -> int:
#         return self._ppl
    
#     def calculate_mission_cost(self) -> float:
#         orbit_radius = self._orbit_height + 6371
#         orbit_circumference = 2 * 3.14159 * orbit_radius
#         fuel_per_mile = self._burn_rate * 2500 / self._orbit_height
#         fuel_per_orbit = fuel_per_mile * orbit_circumference
#         fuel_cost = fuel_per_orbit * self._fuel_cost
#         personnel_cost = self._ppl * self._base_salary
#         mission_cost = fuel_cost + personnel_cost
#         return mission_cost
    
#     def get_full_report(self) -> str:
#         report = f"Spacecraft age: {self.get_age()} years\n"
#         report += f"Spacecraft cost: {self.get_cost()} USD\n"
#         report += f"Spacecraft weight: {self.get_weight()} kg\n"
#         report += f"Spacecraft year built: {self.get_year_built()}\n"
#         report += f"Spacecraft orbit height: {self.get_orbit_height()} miles\n"
#         report += f"Spacecraft burn rate: {self.get_burn_rate()} kg/mile\n"
#         report += f"Fuel cost: {self.get_fuel_cost()} USD/kg\n"
#         report += f"Base salary: {self.get_base_salary()} USD/year/person\n"
#         report += f"Number of person: {self.get_ppl()}\n"
#         report += f"Mission cost: {self.calculate_mission_cost()} USD"
#         return report


# shuttle = SpaceShuttle(cost=1000000000, year_built=2010, weight=200000, orbit_height=400, burn_rate=0.5)
# report = shuttle.get_full_report()
# # Write the report to a file
# with open("report.txt", "w") as f:
#     f.write(report)
# print(shuttle.get_full_report())   
# print("Report saved to file 'report.txt'")

import time

class Carrier:
    """Shuttle cost currency is USD  
    Shutlle weight is in kg   
    Year built should be in this format: YYYY"""
    def __init__(
        self,
        cost: float,
        year_built: int,
        weight: float,
    ) -> None:
        self._cost: float = cost
        self._year_built: int = year_built
        self._weight: float = weight
    def get_age(self) -> int:
        current_timestamp = time.time()
        current_year = time.gmtime(current_timestamp).tm_year
        return current_year - self._year_built
    def get_cost(self) -> float:
        return self._cost
    def get_weight(self) -> float:
        return self._weight

class SpaceShuttle(Carrier):
    CEPAJAV_CONSTANT = 2500
    """Use imperial units for the lenght measurements"""
    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        return self.CEPAJAV_CONSTANT / orbit_height
    def get_fuel_cost(
        self, fuel_cost: float, burn_rate: float, orbit_height: float
    ) -> float:
        burn_rate_variable = self._get_burn_rate_variable(orbit_height)
        return fuel_cost * burn_rate * burn_rate_variable
    def get_average_personel_expenses(
        self, base_salary: float, people_count: int
    ) -> float:
        return base_salary * people_count
    def calculate_mission_cost(
        self,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        base_salary: float,
        people_count: int,
    ) -> float:
        expedition_fuel_cost = self.get_fuel_cost(fuel_cost, burn_rate, orbit_height)
        average_personel_cost = self.get_average_personel_expenses(
            base_salary, people_count
        )
        return expedition_fuel_cost + average_personel_cost



