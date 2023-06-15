from main import Project
from session import session

projektas1 = session.query(Project).get(1)
projektas1.price = 22000
session.commit()

projektas2 = session.query(Project).filter_by(name="2 projektas").one()
projektas2.name = "2 projektas tikrai"
session.commit()