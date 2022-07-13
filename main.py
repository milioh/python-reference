# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "CodersLink SPA FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}