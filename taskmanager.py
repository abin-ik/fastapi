from fastapi import FastAPI,Request

app = FastAPI()

taskM = []

@app.post("/addtask")
async def add_task(request : Request):
    
    data = await request.json()
    
    title = data.get("title")

    status = data.get("status")

    task = {"title" : title , "status" : status}

    taskM.append(task)

    return {f"task added { title } status : { status}"}

@app.get("/gettask")
def get_item():

    return taskM

@app.put("/update1/{index}")
async def update_book(index : int,request:Request):

    if index > 0 and index < len(taskM):

        return  {"invalid index"}
    
    data = await request.json()

    new_task = data.get("taske")

    taskM[index] = new_task

    return {f"task added {new_task}"}

@app.delete("/delete/{index}")
async def delete_book(index : int ):

    if index > 0 and index < len(taskM):

        return {"invalid index"}
    
    deleted = taskM.pop(index)

    return {f"book deleted {deleted}"}




    



    