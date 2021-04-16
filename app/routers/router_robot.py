from fastapi import APIRouter
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
    grid_id: int
    robot_id: int
    instruction: str
    direction: Optional[str] = None

    @validator("instruction")
    def valid_instruction(cls, instruction):
        if instruction not in ["turn", "move", "attack"]:
            raise ValueError("invalid instruction")
        return instruction

    @validator("direction")
    def valid_direction(cls, direction, values):
        if values["instruction"] == "turn" and direction not in ["right", "left"]:
            raise ValueError("invalid direction")
        if values["instruction"] == "move" and direction not in ["forward", "backward"]:
            raise ValueError("invalid direction")

        return direction


class Creation(BaseModel):
    grid_id: int
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


@router.post("/instruction/")
async def instrunction_robot(instruction: Instruction):
    if instruction.instruction == "turn":
        controller_robot.turn(
            instruction.grid_id, instruction.robot_id, instruction.direction
        )
    elif instruction.instruction == "move":
        controller_robot.move(
            instruction.grid_id, instruction.robot_id, instruction.direction
        )
    return instruction


@router.post("/create/")
async def create_robot(creation: Creation):
    robot_id = controller_robot.create(
        creation.grid_id, creation.position_x, creation.position_y, creation.facing
    )
    return {"message": "new robot created!", "robot_id": robot_id}
