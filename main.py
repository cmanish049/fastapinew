from enum import Enum
from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
    {"id": 1, "name": "The Kinks", "genre": "rock"},
    {"id": 2, "name": "The Beatles", "genre": "hip_hop"},
    {"id": 3, "name": "The Rolling Stones", "genre": "electronic"},
    {"id": 4, "name": "The Who", "genre": "metal"},
]

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello, World"}

@app.get("/bands")
async def bands() -> list[dict]:
    return BANDS

@app.get("/bands/{band_id}")
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b["id"] == band_id), None)

    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    
    return band

class GenereURLChoices(Enum):
    ROCK = "rock"
    HIP_HOP = "hip_hop"
    METAL = "metal"
    ELECTRONIC = "electronic"

@app.get("/bands/genere/{genre}")
async def bands_by_genre(genre: GenereURLChoices) -> list[dict]:
    bands = [b for b in BANDS if b["genre"] == genre.value]

    if not bands:
        raise HTTPException(status_code=404, detail="Genre not found")
    
    return bands
