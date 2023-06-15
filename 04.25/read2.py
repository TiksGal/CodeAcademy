from main import Project
from session import session

search = session.query(Project).filter(Project.name.ilike("2%"))
search2 = session.query(Project).filter(Project.price > 1000)
search3 = session.query(Project).filter(
    Project.price > 1000,
    Project.name.ilike("2%"))

print([i for i in search])
print([i for i in search2])
print([i for i in search3])

total_price = 0
for project in search2:
    total_price += project.price
    
print(total_price)


# [2 2 Project - 55000.0: 2021-02-03 14:29:33.477232]
# [1 Naujas pr. - 20000.0: 2021-02-03 14:29:33.437231, 2 2 Project - 55000.0: 2021-02-03 14:29:33.477232]
# [2 2 Project - 55000.0: 2021-02-03 14:29:33.477232]