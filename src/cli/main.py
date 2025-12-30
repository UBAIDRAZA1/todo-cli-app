import argparse
import json
import sys
import os
from typing import List
from src.services.task_service import TaskService

TASKS_FILE = "tasks.json"

def load_tasks_from_file() -> List[dict]:
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks_to_file(tasks: List[dict]):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def main():
    parser = argparse.ArgumentParser(prog="todo", description="Console Todo App")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # list command
    subparsers.add_parser("list", help="List all tasks")

    # update command
    update_parser = subparsers.add_parser("update", help="Update a task description")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="New description")

    # complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    service = TaskService()
    
    # Load existing tasks
    existing_data = load_tasks_from_file()
    service.load_tasks(existing_data)

    if args.command == "add":
        try:
            task = service.add_task(args.description)
            # Implicit success, no output
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.command == "list":
        tasks = service.get_all_tasks()
        for task in tasks:
            status = "[X]" if task.completed else "[ ]"
            print(f"{status} {task.id}. {task.description}")

    elif args.command == "update":
        try:
            task = service.update_task(args.id, args.description)
            if not task:
                print(f"Error: Task with ID {args.id} not found.")
                sys.exit(1)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif args.command == "complete":
        task = service.complete_task(args.id)
        if not task:
            print(f"Error: Task with ID {args.id} not found.")
            sys.exit(1)

    elif args.command == "delete":
        task = service.delete_task(args.id)
        if not task:
            print(f"Error: Task with ID {args.id} not found.")
            sys.exit(1)

    elif args.command is None:
        parser.print_help()
        sys.exit(1)
    
    else:
        print(f"Error: Invalid command.")
        sys.exit(1)

    # Save state
    all_tasks = [t.to_dict() for t in service.get_all_tasks()]
    save_tasks_to_file(all_tasks)

if __name__ == "__main__":
    main()
