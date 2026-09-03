tasks = []


def create_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    return task

def create_task(title):
    if not title.strip():
        raise ValueError("Task title cannot be empty")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    return task