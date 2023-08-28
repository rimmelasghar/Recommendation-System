from pydantic import BaseModel

class MovieIn(BaseModel):
    title: str

class RecommendationResponse(BaseModel):
    movies : list
