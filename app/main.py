from fastapi import FastAPI
from .routers import robot, dinosaur, grid

app = FastAPI()

app.include_router(robot.router)
app.include_router(dinosaur.router)
app.include_router(grid.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
