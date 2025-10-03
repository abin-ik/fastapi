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

@app.put("/ipdate/{index}")

async def update_items(index : int,request :Request):

    if index < 0 and index > len(items):

        return {"error ": " invalid index" }

    data = await request.json()
    new_item = data.get("item")
    items[index] = new_item
    return {"message" : f" succesfullly added {new_item}"}

@app.delete("/delete/{index}")
async def delete_items(index : int):

    if index < 0 and index > len(items):

        return {"error" : " invalid index"}
    
    removed_item = items.pop(index)
    return {"message ": f"removed item is {removed_item}"}


