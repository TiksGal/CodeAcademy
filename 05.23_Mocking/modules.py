from sqlalchemy import Column, String, Integer, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String)
    tasks = relationship("Todo", back_populates="user")

    def __repr__(self) -> str:
        return f"Hello {self.name} {self.surname}"


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    statement = Column("thing to do", String)
    deadline = Column("deadline", DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="tasks")

    def __init__(self, statment, deadline) -> None:
        self.statment = statment
        self.deadline = deadline