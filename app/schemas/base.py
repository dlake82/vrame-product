from pydantic import BaseModel
from typing import Any


class SimpleResponse(BaseModel):
    status: int
    detail: str

class TestResponse(BaseModel):
    status: int
    detail: Any
