# Create a class called Employee with a static method called calculate_payroll 
# that takes a list of Employee instances and returns the total amount to be paid to all employees.
# Each Employee instance has two attributes: name and salary.
from typing import List


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
    
    @staticmethod
    def calculate_payroll(employees: List["Employee"]) -> float:
        return sum(employee.salary for employee in employees)

employees = [Employee("Alice", 5000.0),
             Employee("Bob", 6000.0),
             Employee("Charlie", 7000.0)]
print(Employee.calculate_payroll(employees)) # Output: 18000.0