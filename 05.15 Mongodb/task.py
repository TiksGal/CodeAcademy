from pymongo import MongoClient

class TaskManager:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['task_manager_db']
        self.tasks = self.db.tasks

    def add_task(self) -> None:
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        self.tasks.insert_one({'title': title, 'description': description, 'status': 'in progress'})

    def view_tasks(self) -> None:
        for task in self.tasks.find():
            print(task)

    def update_task_status(self) -> None:
        title = input("Enter the title of the task you want to update: ")
        status = input("Enter the new status: ")
        self.tasks.update_one({'title': title}, {'$set': {'status': status}})

    def delete_task(self) -> None:
        title = input("Enter the title of the task you want to delete: ")
        self.tasks.delete_one({'title': title})

    def main(self) -> None:
        while True:
            operation = input("""
            Please type the operation you want to perform:
            add - Add a new task
            view - View all tasks
            update - Update task status
            delete - Delete a task
            quit - Quit the program
            """)
            if operation == 'add':
                self.add_task()
            elif operation == 'view':
                self.view_tasks()
            elif operation == 'update':
                self.update_task_status()
            elif operation == 'delete':
                self.delete_task()
            elif operation == 'quit':
                break
            else:
                print("Invalid operation. Please try again.")


if __name__ == "__main__":
    TaskManager().main()

