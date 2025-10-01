from fastapi import FastAPI,Request

app = FastAPI()

detail =[]

@app.post("/add")
async def add_item(request:Request):

    data = await request.json()

    name = data.get("name")

    phno = data.get("phone")

    email = data.get("email")

    d = {"name":name , "phone" : phno , "email" : email}

    detail.append(d)

    return {"message":f"{name},{phno},{email}"}

@app.get("/get")
def get_item():

    return {"contacts":detail}