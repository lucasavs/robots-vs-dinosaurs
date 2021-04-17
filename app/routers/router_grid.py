from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator
from ..controllers import controller_grid
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/grid",
    tags=["grid"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates")

@router.post("/create/")
async def create_grid():
    grid_number = controller_grid.create_grid()
    return {"message": "new grid created!", "grid_number": grid_number}


@router.get("/{grid_number}")
async def get_grid(grid_number: int):
    grid = controller_grid.get_grid(grid_number)
    return grid

@router.get("/draw/{grid_id}", response_class=HTMLResponse)
async def draw_grid(request: Request, grid_id: int):
    grid = controller_grid.draw_grid(grid_id)
    return templates.TemplateResponse("grid.html", {"request": request, "grid": grid, "grid_id": grid_id})
