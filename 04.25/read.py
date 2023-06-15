from main import Project
from session import session

projects = session.query(Project).filter_by(name="Naujas pr.").first()

print(projects)