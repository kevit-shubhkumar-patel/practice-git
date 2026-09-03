from fastapi import FastAPI
from app.tasks import create_task

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Task Manager API"}


@app.post("/tasks")
def add_task(title: str):
    return create_task(title)

@app.get("/health")
def health():
    return {"status": "main branch healthy"}