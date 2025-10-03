from fastapi import FastAPI,Request

app = FastAPI()

books = []

@app.post("/addbook")
async def add_book(request : Request):

    data = await request.json()

    title = data.get("title")

    author = data.get("author")

    titles = {"title" : title , "author" : author} 

    books.append(titles)

    return {"message " : f" added books {title} author is {author}"}

@app.get("/getbook")
def get_book():

    return {"message": books}

@app.put("/update/{index}")
async def update_book(index : int, request :Request):

    if index < 0 and index >len(books):

        return {"error": " index out of bounds"}
    
    data = await request.json()

    new_item = data.get("books")

    books[index] =  new_item

    return {"message " : f" added item { new_item} "}

@app.delete("/delete/{index}")
async def delete_book(index : int):

    if index < 0 and index > len(books):

        return {"message" : "ivalid index"}
    
    deleted_book = books.pop(index)

    return {"message": f"item deleted {deleted_book}"}