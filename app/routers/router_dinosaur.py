from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator
from ..controllers import controller_dinosaur

router = APIRouter(
    prefix="/dinosaur",
    tags=["dinosaur"],
    responses={404: {"description": "Not found"}},
)


class Creation(BaseModel):
    grid_id: int
    position_x: int
    position_y: int

    @validator("position_x", "position_y")
    def valid_position(cls, position):
        if position < 0 or position > 49:
            raise ValueError("invalid position")
        return position


@router.post("/create/")
async def create_dinosaur(creation: Creation):
    controller_dinosaur.create(
        creation.grid_id, creation.position_x, creation.position_y
    )
    return {"message": "new dinosaur created!"}
