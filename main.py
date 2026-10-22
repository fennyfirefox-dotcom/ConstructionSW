from fastapi import FastAPI
from app.database import engine, Base
from app.routers import reg, todos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TODO FastAPI",
    description="Simple FastApi todo manager",
    version="1.0.0",
)

app.include_router(reg.router)
app.include_router(todos.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to FastAPI Todo App! Go to /docs for interactive Swagger UI."
    }