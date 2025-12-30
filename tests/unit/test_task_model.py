import pytest
from src.models.task import Task, reset_next_id

@pytest.fixture(autouse=True)
def run_around_tests():
    """Resets Task.next_id before each test to ensure predictable IDs."""
    reset_next_id()
    yield

def test_task_creation_auto_id():
    task1 = Task("Buy groceries")
    assert task1.id == 1
    assert task1.description == "Buy groceries"
    assert not task1.completed

    task2 = Task("Walk the dog")
    assert task2.id == 2
    assert task2.description == "Walk the dog"
    assert not task2.completed

def test_task_creation_with_specified_id():
    task = Task("Read a book", id=10)
    assert task.id == 10
    assert task.description == "Read a book"
    assert not task.completed
    assert Task.next_id == 11 # Ensure next_id updates correctly

def test_task_equality():
    task1 = Task("Task A")
    task1a = Task("Task A", id=1) # Same attributes, same auto-assigned ID
    task2 = Task("Task B")
    task3 = Task("Task A", completed=True)

    assert task1 == task1a
    assert task1 != task2
    assert task1 != task3 # Different completed status

    # Test with manually assigned ID
    task_manual_1 = Task("Manual Task", id=5)
    task_manual_1a = Task("Manual Task", id=5)
    task_manual_2 = Task("Different Manual Task", id=6)

    assert task_manual_1 == task_manual_1a
    assert task_manual_1 != task_manual_2

def test_task_to_dict():
    task = Task("Clean room", id=5, completed=True)
    expected_dict = {"id": 5, "description": "Clean room", "completed": True}
    assert task.to_dict() == expected_dict

def test_task_from_dict():
    data = {"id": 7, "description": "Write report", "completed": False}
    task = Task.from_dict(data)
    assert task.id == 7
    assert task.description == "Write report"
    assert not task.completed
    assert Task.next_id == 8 # Ensure next_id updates correctly after from_dict

def test_task_from_dict_updates_next_id_correctly():
    Task("First task") # id=1
    data = {"id": 10, "description": "High ID task", "completed": False}
    task_high_id = Task.from_dict(data)
    assert Task.next_id == 11 # next_id should be higher than the highest ID seen

    Task("Another task") # id=11
    assert Task.next_id == 12

def test_task_description_only_init():
    task = Task("Simple description")
    assert task.description == "Simple description"
    assert not task.completed
    assert task.id is not None
