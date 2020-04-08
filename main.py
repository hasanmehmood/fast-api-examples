import shutil
from pathlib import Path
from fastapi import FastAPI, File, UploadFile

from models.Item import Item


app = FastAPI()


# --- Hello World
@app.get("/")
def read_root():
    return {"Hello": "World"}


# --- Recieving id:int along with query params in variable q
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# --- upgrade example. we will receive payload via PUT
# If the request payload miss any required attr then auto
# error will send back along with the error message
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# --- File Upload and Saving 
# https://github.com/tiangolo/fastapi/issues/426
def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


# Using UploadFile
@app.post("/uploadfile/")
def create_upload_file(file: UploadFile = File(...)):
    filepath = Path('uploaded_folder') / file.filename
    save_upload_file(file, filepath)
    return {"filename": file.filename}


# Using bytes
@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}
