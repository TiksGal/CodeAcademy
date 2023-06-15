from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from modules import User, Todo
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def create_detabase(self) -> None:
        pass

    @abstractmethod
    def create_user(self, name: str, surname: str, email: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def check_authentification(self, user: User, password: str) -> bool:
        pass

    @abstractmethod
    def add_task(self, statement: str, deadline: datetime, user: User) -> None:
        pass

    @abstractmethod
    def get_tasks(self, user: User) -> str:
        pass

    @abstractmethod
    def update_task(self, task_id: int, user: User, text: str) -> None:
        pass

    @abstractmethod
    def update_task_deadline(
        self, task_id: int, user: DeclarativeMeta, deadline: datetime
    ) -> None:
        pass

    @abstractmethod
    def delete_task(self, task_id: int, user: DeclarativeMeta) -> None:
        pass


class SqliteDatabase(Database):
    def __init__(self, filename: str, base: DeclarativeMeta):
        self.filename = filename
        self.Base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_detabase(self) -> None:
        self.Base.metadata.create_all(self.engine, checkfirst=True)

    def create_user(self, name: str, surname: str, email: str, password: str) -> None:
        user = User(name=name, surname=surname, email=email, password=password)
        self.session.add(user)
        self.session.commit()

    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter_by(email=email).first()

    def check_authentification(self, user: User, password: str) -> bool:
        if password == user.password:
            return True
        else:
            return False

    def add_task(self, statement: str, deadline: datetime, user: User) -> None:
        task = Todo(statment=statement, deadline=deadline)
        user.tasks.append(task)
        self.session.add(task)
        self.session.commit()

    def get_tasks(self, user: User) -> str:
        return user.tasks

    def update_task(self, task_id: int, user: User, text: str) -> None:
        for item in user.tasks:
            if task_id == item.id:
                item.statment = text
                self.session.commit()

    def update_task_deadline(
        self, task_id: int, user: DeclarativeMeta, deadline: datetime
    ) -> None:
        for item in user.tasks:
            if task_id == item.id:
                item.deadline = deadline
                self.session.commit()

    def delete_task(self, task_id: int, user: DeclarativeMeta) -> None:
        for item in user.tasks:
            if task_id == item.id:
                self.session.delete(item)
                self.session.commit()

class TestDatabase(Database):
    def create_user(self, name: str, surname: str, email: str, password: str) -> None:
        None
        
    def get_user_by_email(self, email):
        return 
    
    
    def create_detabase(self) -> None:
        pass


    def check_authentification(self, user: User, password: str) -> bool:
        pass

    def add_task(self, statement: str, deadline: datetime, user: User) -> None:
        pass

    def get_tasks(self, user: User) -> str:
        pass

    def update_task(self, task_id: int, user: User, text: str) -> None:
        pass

    def update_task_deadline(
        self, task_id: int, user: DeclarativeMeta, deadline: datetime
    ) -> None:
        pass

    def delete_task(self, task_id: int, user: DeclarativeMeta) -> None:
        pass