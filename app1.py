from fastapi import FastAPI,Request

app = FastAPI()

tasks = []

@app.post("/add")
async def add_itmes(request : Request):

    data = await request.json()

    title = data.get("title")

    completed = data.get("completed")

    task = {"title":title,"groceries":completed}

    tasks.append(task)

    return {"message":f"succesfully added {title},{completed}"}

@app.get("/get")
def get_items():

    return {"tasks" : tasks}
    



