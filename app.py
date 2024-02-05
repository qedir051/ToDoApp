class ToDoApp:
    def __init__(self):
        self.task_list = []
        self.case = True

    def add_task(self):
        # Adding tasks to the list
        task = input("Type the task:")
        self.task_list.append(task)
        print(f"{task}  successfully added.")

    def view_task(self):
        # While there's at least one task
        if len(self.task_list) > 0:
            for index, task in enumerate(self.task_list):
                print(f"{index}. {task}")
        else:
            print("There's not anything to show!")

    def remove_task(self):
        if len(self.task_list) > 0:
            task_index = -1
            while task_index < 0 or task_index >= len(self.task_list):  # to deal with error of Out of Range
                task_index = int(
                    input(f"Enter task index(between 0-{len(self.task_list) - 1}) which you want to remove: "))
                if not (0 <= task_index < len(self.task_list)):
                    print("Type Valid index!")
                    continue
            # To be sure of removing that element or not
            while True:
                prompt = input(f"Are you sure to delete {self.task_list[task_index]}?Y/N: ").upper()

                match prompt:
                    case 'Y':
                        print(f"Order executed! {self.task_list[task_index]} removed.")
                        self.task_list.pop(task_index)
                        break
                    case 'N':
                        print("Returns to the Menu.")
                        self.menu_options()
                        break
                    case _:
                        print("Wrong input! Type only Y or N")
                        continue

        else:       # If there is not any task
            print("There's nothing in the list!")

    def app(self):
        print("Hello to my To Do app!")
        while self.case:
            self.menu_options()

    def menu_options(self):
        self.case = True     # Checking of running of program
        prompt = -1
        while prompt not in ['add', 'view', 'remove', 'exit']:     # Getting right input by user
            prompt = input("What do you want?"
                           "add for adding task/view for viewing task/remove for removing task/"
                           "exit for closing app: ").lower()
            if prompt not in ['add', 'view', 'remove', 'exit']:
                print("Enter valid prompt! add/view/remove/exit")

        if prompt == "add":
            self.add_task()

        elif prompt == "view":
            self.view_task()

        elif prompt == "remove":
            self.remove_task()

        elif prompt == "exit":
            print("Program stopped. Thanks for using it.")
            self.case = False


if __name__ == "__main__":
    my_app = ToDoApp()
    my_app.app()
