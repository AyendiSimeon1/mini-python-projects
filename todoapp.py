
class Todo:

    def __init(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    #def removeTask(self, task):
    def viewTask(self, task):
        for i in self.tasks:
            print("These are the tasks")
            print(i)

        else:
            print("Your task list is empty")

def main():
    app = Todo()

    while True:
        print("Welcome to the Ayendi Task list")
        print("Enter 1 to view task")
        print("Enter 2 to add task")
        print("Enter 3 to delete task")

        choice = input("Enter Your Choice Here")

        if choice == "1":
            print("These are all the tasks available")
            app.viewTask
        elif choice == "2":
            print("Add a task")
            newTask = input("Enter your new task: ")
            app.addTask(newTask)

        else:
            break

if __name__ == "__main__":
    main()
        
