class Employee:
    def __init__(self, first_name: str, last_name: str) -> str:
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{self.first_name} {self.last_name}"
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

# Create an instance of the Employee class
employee = Employee("Darbo", "Zmogus")

print(employee.fullname)  
print(employee.email)  
