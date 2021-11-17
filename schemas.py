from pydantic import BaseModel, validator
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

    @validator("age")
    def check_age(cls, v):
        if v < 15:
            raise ValueError("Author age must be more than 15!")
        return v

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]