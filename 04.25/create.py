from main import Project
from session import session

projektas1 = Project("Naujas pr.", 20000)
session.add(projektas1)
session.commit()

projektas2 = Project("2 projektas", 55000)
session.add(projektas2)
session.commit()