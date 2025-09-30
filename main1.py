from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message":"welcome to math API"}

@app.get("/multiply/{number}")
def mul(number:int):

    result = number*5

    return {f"message": {number}, "result": {result}}

@app.get("/square/{number}")
def square(number:int):

    result = number**2

    return {f"message": {number}, "result": {result}}