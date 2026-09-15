def add_task(tasks, employee, task, status):
    """Add a task dict to the tasks list after basic validation.

    Raises:
        ValueError: if employee or task is empty.
    """
    if not employee or not task:
        raise ValueError("Employee and task are required")

    tasks.append({
        "Employee": employee,
        "Task": task,
        "Status": status
    })

    return tasks
