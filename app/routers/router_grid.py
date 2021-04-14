from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator
from ..controllers import controller_grid
from fastapi import FastAPI, HTTPException

router = APIRouter(
    prefix="/grid",
    tags=["grid"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create/")
async def create_grid():
    grid_number = controller_grid.create_grid()
    return {
        "message": "new grid created!",
        "grid_number": grid_number
    }

@router.get("/{grid_number}")
async def get_grid(grid_number: int):
    grid = controller_grid.get_grid(grid_number)
    return grid
