# Endpoints to create:
# ⿡ POST /addmovie
#     - Accepts JSON body:
#       {
#         "name": "Inception",
#         "rating": 9
#       }
#     - Adds a new movie to the list.
#
# ⿢ GET /getmovies
#     - Returns all movies.
#
# ⿣ PUT /updatemovie/{index}
#     - Updates a movie's name or rating by index.
#
# ⿤ DELETE /deletemovie/{index}
#     - Deletes a movie by index.
#
# Requirements:
# - Each movie should have:
#     - "name" (string)
#     - "rating" (integer between 1 and 10)
# - If the rating is outside this range, return an error message.

from fastapi import FastAPI,Request

app = FastAPI()

movies = []

@app.post("/addmovie")
async def add_movie(request : Request):

    data = await request.json()

    movie = data.get("movie")

    rating = data.get("rating")

    title = {"movie" : movie , "rating" : rating}

    movies.append(title)

    return {"message" : f"{movies}"}

@app.get("/getmovie")
def get_movie():

    return {"message":movies}

@app.put("/up/{index}")
async def update_movie(index:int,request : Request):

    if index < 0 and index > len(movies):

        return {"invalid index"}
    
    data = await request.json()

    new_item = data.get("mov")

    movies[index] = new_item

    return {"message": f" {new_item}"}

@app.delete("/delete/{index}")
async def delete_movie(index: int):

    if index < 0 and index > len(movies):

        return {"invalid index"}
    
    deleted = movies.pop(index)

    return {"message": f"{deleted}"}






