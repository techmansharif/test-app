from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AddRequest(BaseModel):
    a: int
    b: int

class AddResponse(BaseModel):
    result: int

@router.post("/add", response_model=AddResponse)
async def add_numbers(data: AddRequest):
    print(data)
    return AddResponse(result=data.a + data.b)
