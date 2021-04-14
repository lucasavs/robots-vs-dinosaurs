from fastapi import FastAPI
from .routers import router_robot, router_dinosaur, router_grid

app = FastAPI()

app.include_router(router_robot.router)
app.include_router(router_dinosaur.router)
app.include_router(router_grid.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
