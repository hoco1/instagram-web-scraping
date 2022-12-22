import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/",tags=["test"])
def greet():
    return {"Hello":"World!"}