import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# --- Hello World
@app.get("/")
def read_root():
    return {"Hello": "World"}



# --- Recieving id:int along with query params in variable q
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

