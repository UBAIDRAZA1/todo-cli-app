# CLI Commands Definition: Phase I – Console Todo App

**Date**: 2025-12-27

This document defines the command-line interface (CLI) commands, their syntax, arguments, and expected behavior. All commands follow the `todo <command> [arguments]` format.

## Commands:

### 1. `todo add "<description>"`

- **Purpose**: Adds a new task to the todo list.
- **Arguments**:
  - `<description>` (string, required): The task's textual content. Must be enclosed in double quotes if it contains spaces.
- **Behavior**:
  - Creates a new `Task` object with a unique ID, the provided description, and `completed` status as `false`.
  - Allows for duplicate task descriptions (FR-001).
  - Assigns a new, unique, sequential integer ID to the task.
- **Success Output**: No explicit output (implicit success is that `todo list` will show the new task).
- **Error Output**:
  - "Error: Description cannot be empty." if `<description>` is empty.

### 2. `todo list`

- **Purpose**: Displays all tasks in the todo list.
- **Arguments**: None.
- **Behavior**:
  - Retrieves all `Task` objects from in-memory storage.
  - Displays tasks in the order they were added, or by ID.
- **Success Output**: A formatted list of tasks, one per line. Completed tasks are prefixed with `[X]`, pending with `[ ]`. Example:
  ```
  [X] 1. Buy milk
  [ ] 2. Walk the dog
  [X] 3. Call mom
  ```
- **Error Output**: None (even if the list is empty, it should just show an empty list).

### 3. `todo update <task_id> "<new_description>"`

- **Purpose**: Updates the description of an existing task.
- **Arguments**:
  - `<task_id>` (integer, required): The unique ID of the task to update.
  - `<new_description>` (string, required): The new textual content for the task. Must be enclosed in double quotes if it contains spaces.
- **Behavior**:
  - Finds the `Task` by `<task_id>`.
  - Updates its `description` attribute.
  - If `<task_id>` does not exist, shows an error (FR-009).
- **Success Output**: No explicit output (implicit success is that `todo list` will show the updated task).
- **Error Output**:
  - "Error: Task with ID <task_id> not found." if `task_id` does not exist.
  - "Error: Description cannot be empty." if `<new_description>` is empty.

### 4. `todo complete <task_id>`

- **Purpose**: Marks an existing task as complete.
- **Arguments**:
  - `<task_id>` (integer, required): The unique ID of the task to mark complete.
- **Behavior**:
  - Finds the `Task` by `<task_id>`.
  - Sets its `completed` attribute to `true`.
  - If `<task_id>` does not exist, shows an error (FR-009).
- **Success Output**: No explicit output (implicit success is that `todo list` will show the task as completed).
- **Error Output**:
  - "Error: Task with ID <task_id> not found." if `task_id` does not exist.

### 5. `todo delete <task_id>`

- **Purpose**: Deletes an existing task from the todo list.
- **Arguments**:
  - `<task_id>` (integer, required): The unique ID of the task to delete.
- **Behavior**:
  - Finds the `Task` by `<task_id>`.
  - Removes the `Task` from in-memory storage.
  - If `<task_id>` does not exist, shows an error (FR-009).
- **Success Output**: No explicit output (implicit success is that `todo list` will no longer show the task).
- **Error Output**:
  - "Error: Task with ID <task_id> not found." if `task_id` does not exist.
