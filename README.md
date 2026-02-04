## Task tracker
```
# Initial setup
# Create and activate the virtual environment
python3 -m venv .venv
. ./.venv/bin/activate

# Installation
pip3 install .

# Exit the virtual environment
deactivate

# Uninstallation
pip3 uninstall task_tracker
```
```
# Adding a new task
task_tracker add "Buy groceries"

# Updating a task
task_tracker update 1 "Buy groceries and cook dinner"

# Deleting a tasks
task_tracker delete 1

# Marking a task as in progress or done
task_tracker mark-in-progress 1
task_tracker mark-done 1

# Listing all tasks
task_tracker list

# Listing tasks by status
task_tracker list done
task_tracker list todo
task_tracker list in-progress
```
