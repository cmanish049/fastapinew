from fastapi import FastAPI, HTTPException
from schemas import GenereURLChoices
from schemas import Band
from typing import Union

app = FastAPI()

BANDS = [
    {"id": 1, "name": "The Kinks", "genre": "rock"},
    {"id": 2, "name": "The Beatles", "genre": "hip_hop"},
    {"id": 3, "name": "The Rolling Stones", "genre": "electronic"},
    {"id": 4, "name": "The Who", "genre": "metal", "albums": [
        {"title": "My Generation", "release_date": "1965-12-03"},
        {"title": "A Quick One", "release_date": "1966-12-09"},
        {"title": "The Who Sell Out", "release_date": "1967-12-15"},
    ]},
]

@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello, World"}

@app.get("/bands")
async def bands(
    genre: Union[GenereURLChoices, None] = None,
    has_albums: bool = False
) -> list[Band]:
    band_list = [
        Band(**band) for band in BANDS
    ]

    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    
    if has_albums:
        band_list = [
            band for band in band_list if len(band.albums) > 0
        ]
    
    return band_list

@app.get("/bands/{band_id}")
async def band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b["id"] == band_id), None)

    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    
    return band