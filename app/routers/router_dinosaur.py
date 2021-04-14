from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator

router = APIRouter(
    prefix="/dinosaur",
    tags=["dinosaur"],
    responses={404: {"description": "Not found"}},
)


class Creation(BaseModel):
    position_x: int
    position_y: int

    @validator("position_x", "position_y")
    def valid_position(cls, position):
        if position < 0 or position > 49:
            raise ValueError("invalid position")


@router.post("/create/")
async def instrunction_robot(creation: Creation):
    return creation
    # raise NotImplemented
