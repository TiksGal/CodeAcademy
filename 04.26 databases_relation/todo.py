# Create a TO DO list application that runs in terminal. It should allow user to log in. 
# Each user should have his own tasks in to do list. 
# User should be able to add/ update/ delete tasks. User information and task information should be kept in database

from todo_classes import Database, Application


def main() -> None:
    db = Database()
    app = Application(db)
    app.run()


if __name__ == "__main__":
    main()

