from typing import Optional

class Task:
    """
    Represents a single todo item.
    """
    next_id: int = 1

    def __init__(self, description: str, id: Optional[int] = None, completed: bool = False):
        if id is None:
            self.id = Task.next_id
            Task.next_id += 1
        else:
            self.id = id
            # Ensure next_id is always greater than any manually assigned ID
            if id >= Task.next_id:
                Task.next_id = id + 1
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.id == other.id and self.description == other.description and self.completed == other.completed

    def to_dict(self):
        return {"id": self.id, "description": self.description, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(id=data["id"], description=data["description"], completed=data["completed"])

# Reset next_id for testing or re-initialization purposes
def reset_next_id():
    Task.next_id = 1
