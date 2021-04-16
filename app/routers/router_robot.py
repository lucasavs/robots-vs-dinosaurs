from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator
from typing import Optional
from ..controllers import controller_robot

# from .. import grid

router = APIRouter(
    prefix="/robot",
    tags=["robot"],
    responses={404: {"description": "Not found"}},
)


class Instruction(BaseModel):
    instruction: str
    direction: Optional[str] = None

    @validator("instruction")
    def valid_instruction(cls, instruction):
        if instruction not in ["turn", "move", "attack"]:
            raise ValueError("invalid instruction")

    @validator("direction")
    def valid_direction(cls, direction):
        if direction not in ["right", "left"]:
            raise ValueError("invalid direction")


class Creation(BaseModel):
    grid: int
    position_x: int
    position_y: int
    facing: str

    @validator("position_x", "position_y")
    def valid_position(cls, position):
        if position < 0 or position > 49:
            raise ValueError("invalid position")
        return position

    @validator("facing")
    def valid_direction(cls, facing):
        if facing not in ["up", "down", "right", "left"]:
            raise ValueError("invalid facing direction")
        return facing


@router.post("/instruction/{robot_id}")
async def instrunction_robot(robot_id: int, instruction: Instruction):
    return instruction
    # raise NotImplemented


@router.post("/create/")
async def create_robot(creation: Creation):
    controller_robot.create_robot(
        creation.grid, creation.position_x, creation.position_y, creation.facing
    )
    return {"message": "new robot created!"}
