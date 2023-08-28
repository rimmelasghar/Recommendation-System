import pickle
import re
from pathlib import Path
import pandas as pd

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/model-{__version__}.pkl", "rb") as file:
    model = pickle.load(file)

with open(f"{BASE_DIR}/IMDB-{__version__}.pkl", "rb") as movie:
    df = pickle.load(movie)

movies = pd.DataFrame(df)

def recommend(movie):
    try:
        movie_index  = movies[movies['title'] == movie].index[0] # Index of movie you selected
        recom = sorted(list(enumerate(model[movie_index])), reverse = True, key = lambda x : x[1])[1 : 11] # You will get indexes of recommended movies
        rec_movies = []
        
        for i in recom:
        # Get Names of Recommended Movies
            rec_movies.append(movies.iloc[i[0]].title) #All the recommeded movie titles saved in a list

        return rec_movies
    except:
        return None

print(recommend('Superman21he'))
