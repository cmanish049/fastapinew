from enum import Enum
from datetime import date
from pydantic import BaseModel

class GenereURLChoices(Enum):
    ROCK = "rock"
    HIP_HOP = "hip_hop"
    METAL = "metal"
    ELECTRONIC = "electronic"

class Album(BaseModel):
    title: str
    release_date: date

class Band(BaseModel):
    id: int
    name: str
    genre: str
    albums: list[Album] = []