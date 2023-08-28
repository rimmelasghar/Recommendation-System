from fastapi import APIRouter
from .schemas import MovieIn,RecommendationResponse
from .service import recommendation
import os
from .contants import *

router = APIRouter()

@router.get("/status")
async def status():
    return {"status":"running","mode":ENVIROMENT,"version":VERSION}

@router.post("/movies/recommendation", response_model=RecommendationResponse)
async def movie_recommendation(movie: MovieIn):
    return recommendation(movie)
