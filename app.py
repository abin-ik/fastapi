from fastapi import FastAPI,Request

app = FastAPI()

items = []

@app.post("/additems")

async def add_items(request : Request):

    data = await request.json()  # read the request body as Json

    item = data.get("item")

    items.append(item)

    return {"message":f" succesfully added item {item}"}

@app.get("/getitems")

def get_itmes():

    return {"items ": items}

