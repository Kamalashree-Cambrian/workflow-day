from task_manager import add_task


def test_add_task():
    tasks = []

    result = add_task(
        tasks,
        "Kamal",
        "Prepare report",
        "To Do"
    )

    assert len(result) == 1
    assert result[0]["Employee"] == "Kamal"
    assert result[0]["Status"] == "To Do"


def test_add_task_missing_employee_raises():
    tasks = []
    try:
        add_task(tasks, "", "Prepare report", "To Do")
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_add_task_missing_task_raises():
    tasks = []
    try:
        add_task(tasks, "Kamal", "", "To Do")
        assert False, "expected ValueError"
    except ValueError:
        pass
