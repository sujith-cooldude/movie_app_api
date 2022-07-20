from common_operations import get_movie_info, get_movie_result
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"hello": "world"}


@app.get("/get_recomended_movies/{city}")
async def get_recomended_movies(city):
    result = get_movie_result(city)
    return {"data": result}

@app.get("/get_latest_movies/{city}")
async def get_latest_movies(city):
    result = get_movie_info(city)
    return {"data": result}
