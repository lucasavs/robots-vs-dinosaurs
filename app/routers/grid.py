from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, validator

router = APIRouter(
    prefix="/grid",
    tags=["grid"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create/")
async def instrunction_robot():
    raise NotImplementedError("not implemented")
