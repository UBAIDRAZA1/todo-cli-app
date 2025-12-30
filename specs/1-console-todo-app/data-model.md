# Data Model: Phase I – Console Todo App

**Date**: 2025-12-27

## Entity: Task

Represents a single todo item within the application.

### Attributes:

- **`id` (integer)**:
  - **Description**: A unique identifier for the task. Automatically assigned sequentially upon creation.
  - **Constraints**: Must be a positive integer. Unique across all active tasks.
- **`description` (string)**:
  - **Description**: The textual content of the task.
  - **Constraints**: Must not be empty (handled as an edge case: `todo add ""` will be addressed in Polish phase). Can contain any Unicode characters. Max length 255 characters (assumption for now, can be clarified later if needed).
- **`completed` (boolean)**:
  - **Description**: A flag indicating whether the task has been marked as complete.
  - **Default Value**: `false` (pending) upon creation.
  - **State Transitions**: Can change from `false` to `true` via `todo complete <id>`. Cannot be undone in Phase I.

### Relationships:

- None (Task is a standalone entity in Phase I).

### Validation Rules:

- `id`: Must be a valid integer, and the task must exist for update, complete, and delete operations.
- `description`: Must not be empty.
