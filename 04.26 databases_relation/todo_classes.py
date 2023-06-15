from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from typing import Optional
import os

os.environ["SQLALCHEMY_SILENCE_UBER_WARNING"] = "1"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")


class Database:
    def __init__(self, db_url: str = "sqlite:///todo_app.db"):
        self.engine = create_engine(db_url)
        self.session = sessionmaker(bind=self.engine)

    def create_database(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.session()

    def login(self, username: str) -> User:
        session = self.get_session()
        user = session.query(User).filter(User.username == username).first()
        if not user:
            user = User(username=username)
            session.add(user)
            session.commit()
        user.session = session
        return user

    def add_task(self, user: User, description: str) -> None:
        task = Task(description=description, user=user)
        session = user.session
        session.add(task)
        session.commit()

    def delete_task(self, user: User, task_id: int) -> None:
        session = user.session
        task = session.query(Task).filter(Task.user_id == user.id, Task.id == task_id).first()

        if task:
            session.delete(task)
            session.commit()
        else:
            print("Task not found")

    def update_task(self, user: User, task_id: int, new_description: str) -> None:
        session = user.session
        task = session.query(Task).filter(Task.user_id == user.id, Task.id == task_id).first()

        if task:
            task.description = new_description
            session.commit()
        else:
            print("Task not found")

    def list_tasks(self, user: User) -> None:
        session = user.session
        tasks = session.query(Task).filter(Task.user_id == user.id).all()

        for task in tasks:
            print(f"{task.id}: {task.description}")


class Application:
    def __init__(self, database: Database):
        self.db = database
        self.user = None

    def login(self) -> None:
        username = input("Enter your username to log in: ")
        self.user = self.db.login(username)
        print(f"Welcome {self.user.username}!")

    def add_task(self) -> None:
        description = input("Enter task description: ")
        self.db.add_task(self.user, description)

    def update_task(self) -> None:
        task_id = int(input("Enter task ID to update: "))
        new_description = input("Enter new task description: ")
        self.db.update_task(self.user, task_id, new_description)

    def delete_task(self) -> None:
        task_id = int(input("Enter task ID to delete: "))
        self.db.delete_task(self.user, task_id)

    def list_tasks(self) -> None:
        self.db.list_tasks(self.user)

    def run(self) -> None:
        self.db.create_database()

        exit_app = False
        while not exit_app:
            self.login()

            while True:
                print("\nAvailable actions:")
                print("1. Add task")
                print("2. Update task")
                print("3. Delete task")
                print("4. List tasks")
                print("5. Log out")
                choice = input("Choose an action: ")

                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.update_task()
                elif choice == "3":
                    self.delete_task()
                elif choice == "4":
                    self.list_tasks()
                elif choice == "5":
                    exit_app = True
                    break
                else:
                    print("Invalid option. Please try again.")