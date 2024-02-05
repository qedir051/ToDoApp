# To-Do App

A simple console-based To-Do app written in Python.

## Features
- **Add Task:** Add tasks to your to-do list.
- **View Tasks:** Display all tasks in your to-do list.
- **Remove Task:** Remove a task from your to-do list with confirmation.

## Getting Started
### Installation
1. Clone the repository to your local machine.

### Run the App
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run `python your_script_name.py` (replace your_script_name with the actual name of your Python script).

### Using the App
- Follow the on-screen prompts.
- Type `add` to add a new task, `view` to view your tasks, `remove` to remove a task, and `exit` to close the app.

## How to Use
### Adding a Task
1. Type `add` when prompted.
2. Enter the task details as instructed.

### Viewing Tasks
1. Type `view` when prompted.
2. Your tasks will be displayed with an index.

### Removing a Task
1. Type `remove` when prompted.
2. Enter the index of the task you want to remove.
3. Confirm your decision with `Y` or `N`.

### Exiting the App
- Type `exit` when prompted to close the app.

## Example
```python
Hello to my To-Do app!

What do you want? (add/view/remove/exit): add
Type the task: Task 1
Task 1 successfully added.

What do you want? (add/view/remove/exit): view
0. Task 1

What do you want? (add/view/remove/exit): remove
Enter task index (between 0-0) which you want to remove: 0
Are you sure to delete Complete README file? Y/N: Y
Order executed! Task 1 removed.

What do you want? (add/view/remove/exit): exit
Program stopped. Thanks for using it.
```

### Contributing
Feel free to contribute by opening issues or submitting pull requests.

### License
This project is licensed under the MIT License.
