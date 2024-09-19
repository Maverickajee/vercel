from fastapi import FastAPI

app = FastAPI()

@app.get('/tasks')
def read_tasks():
    return {'tasks': ['Task 1', 'Task 2', 'Task 3']}
