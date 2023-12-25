
class Todo:

    def __init__(self):
        self.tasks = ['no need']

    def addTask(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')
        print('----------------------------')

    def viewTask(self):
        if not self.tasks:
            print('No task available')

        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}, {task}')
                print('-----------------------')

    def deleteTask(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print('Invalid task index.')
def main():
    app = Todo()

    while True:
        print('-----------------------------------------')
        print("Create, View, and Delete Your Tasks Here")
        print("Enter 1 to Create a task")
        print("Enter 2 to View tasks")
        print("Enter 3 to delete task")
        print("Enter 4 to exit")

        choice = input("Enter Your Choice Here:")

        if choice == "1":
            print("Add a task here")
            task = input("Enter your new task: ")
            app.addTask(task)

            
        elif choice == "2":
            
            app.viewTask()
            print("These are all the tasks available")
        
        elif choice == "3":
            app.deleteTask()
        
        elif choice == "4":
            break

        else:
            print('Enter a valid input.')

if __name__ == "__main__":
    main()
        
