from .schemas import MovieIn,RecommendationResponse
from .exceptions import MovieNotFound
from src.model.model import recommend

def recommendation(movie: MovieIn) -> RecommendationResponse:
    movies = recommend(movie.title)
    if movies:
        print(movies)
        return RecommendationResponse(movies=movies)
    raise MovieNotFound()
    