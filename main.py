from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# base example
@app.get("/")
async def root():
    return {"message": "Hello World"}

# my own example
@app.get("/a")
def home():
    return "<h1>hola</h1>"

# parameter example
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# enum example with parameter
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return open(file_path, "r").read()

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

templates = Jinja2Templates(directory="templates")

@app.get("/home", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
