from app.tasks import create_task


def test_create_task():
    task = create_task("Learn Git")

    assert task["title"] == "Learn Git"
    assert task["completed"] is False