# Quickstart: Phase I – Console Todo App

**Date**: 2025-12-27

This guide will help you set up, run, and test the Phase I Console Todo App.

## 1. Setup

The project uses Python 3.11. It is recommended to use a virtual environment.

```bash
# Clone the repository (if not already done)
# git clone <repository_url>
# cd phase2/

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install dependencies (pytest for testing, etc.)
pip install pytest
```

## 2. Running the Application

The main entry point for the CLI application is `app.py`.

```bash
# Add a task
python app.py add "Buy groceries"
python app.py add "Walk the dog"

# List tasks
python app.py list

# Mark a task complete (assuming ID 1 for "Buy groceries")
python app.py complete 1

# Update a task (assuming ID 2 for "Walk the dog")
python app.py update 2 "Walk the cat"

# List tasks again to see changes
python app.py list

# Delete a task (assuming ID 3 for "Call mom" if it was added)
# python app.py delete 3

# Try an invalid command
python app.py unknown-command
```

## 3. Running Tests

Tests are located in the `tests/` directory and use `pytest`.

```bash
# Ensure your virtual environment is active
# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Run all tests
pytest

# To run specific tests, e.g., unit tests for the Task model
pytest tests/unit/test_task_model.py
```
