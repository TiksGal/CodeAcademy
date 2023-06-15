from modules import User, Todo, Base
from database import SqliteDatabase, Database
from welcome import welcome
from datetime import datetime
from typing import Optional



def register_user(db: Database) -> User:
    name = input("Please define your name: ")
    surname = input("Please define surname: ")
    email = input("Please define email: ")
    password = input("Please define password: ")
    db.create_user(name=name, surname=surname, email=email, password=password)
    return db.get_user_by_email(email)
    
if __name__ == "__main__":
    db = SqliteDatabase("test.db", Base)
    db.create_detabase()

    welcome()
    def app() -> Optional[User]:
        is_on = True
        while is_on:
            print("\n1- Register account \n2- Login \n3- Exit")
            option = int(input("Please choose your action: "))
            if option == 1:
                register_user(db)

            if option == 2:
                entered_email = input("Email: ")
                user = db.get_user_by_email(entered_email)
                password = input("Password:")
                if db.check_authentification(user, password) == True:
                    print("Password correct!")
                    return user
                else:
                    print("Incorect password!")

            if option == 3:
                is_on = False


    def get_to_do_list() -> None:
        user = app()
        if user == None:
            is_on = False
        else:
            is_on = True
        while is_on:
            print(
                "\n1- Create task for user \n2- Show tasks assigned for user \n3- Update task \n4- Update deadline \n5- Delete task \n6- I am done!"
            )
            option = int(input("Please specify your selection:"))
            if option == 1:
                statement = input("Please describe task:")
                deadline = datetime.strptime(
                    input("Please enter the deadline (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                db.add_task(statement, deadline)

            if option == 2:
                for item in db.get_tasks(user):
                    print(item.id)
                    print(item.statement)
                    print(item.deadline)

            if option == 3:
                id_to_modify = int(input("Please define which statement ID to change: "))
                new_statement = input("Please set new statement: ")
                db.update_task(id_to_modify, user, new_statement)

            if option == 4:
                id_to_modify = int(input("Please define which statement ID to change: "))
                new_deadline = datetime.strptime(
                    input("Please enter the deadline (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                db.update_task_deadline(id_to_modify, user, new_deadline)

            if option == 5:
                id_to_modify = int(input("Please define statement ID to delete: "))
                db.delete_task(id_to_modify, user)

            if option == 6:
                is_on = False


    get_to_do_list()