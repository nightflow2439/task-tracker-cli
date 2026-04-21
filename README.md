# Task Tracker CLI

A simple command-line task tracker for managing your to-do tasks.

## Usage

### Method 1: Run Directly

Use Python to run the program with commands:

`python main.py <command> [arguments]`

### Method 2: Global Command (Windows)

1. Add the program folder to your user PATH. 
(program folder example: C:\Users\Administrator\Desktop\workspace\task-tracker-cli)
2. In any terminal, use:

`task-cli <command> [arguments]`

## Commands

- `add <task_name>`: Add a new task
- `update <task_id> <new_task_name>`: Update a task's name
- `delete <task_id>`: Delete a task
- `mark-in-progress <task_id>`: Mark a task as in progress
- `mark-done <task_id>`: Mark a task as done
- `list`: List all tasks
- `list <todo|in-progress|done|not-done>`: List tasks by status

## Uninstall

Remove the path of `main.py` from your PATH in user environment variables.

## Project URL

https://roadmap.sh/projects/task-tracker
