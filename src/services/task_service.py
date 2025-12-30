from typing import List, Optional
from src.models.task import Task, reset_next_id

class TaskService:
    def __init__(self):
        self._tasks: List[Task] = []
        reset_next_id() # Ensure IDs are reset for a fresh service instance

    def add_task(self, description: str) -> Task:
        if not description:
            raise ValueError("Description cannot be empty.")
        task = Task(description)
        self._tasks.append(task)
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in self._tasks if task.id == task_id), None)

    def get_all_tasks(self) -> List[Task]:
        return sorted(self._tasks, key=lambda task: task.id)

    def update_task(self, task_id: int, new_description: str) -> Optional[Task]:
        if not new_description:
            raise ValueError("Description cannot be empty.")
        task = self.get_task_by_id(task_id)
        if task:
            task.description = new_description
        return task

    def complete_task(self, task_id: int) -> Optional[Task]:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
        return task

    def delete_task(self, task_id: int) -> Optional[Task]:
        task_to_delete = self.get_task_by_id(task_id)
        if task_to_delete:
            self._tasks.remove(task_to_delete)
        return task_to_delete

    def load_tasks(self, tasks_data: List[dict]):
        """Loads tasks from a list of dictionaries, preserving IDs."""
        self._tasks = []
        # Reset ID counter before loading to ensure it catches up correctly
        reset_next_id()
        for data in tasks_data:
            task = Task.from_dict(data)
            self._tasks.append(task)
