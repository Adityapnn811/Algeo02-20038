from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks, Form
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os
import uuid
import json
import sys
sys.path.append('svd')
import main

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/") #slash bermaksud url dasar seperti local host 8000
def root(request : Request):
    return templates.TemplateResponse("index.html",{"request" : request})

@app.post("/api/v1/convert_image")
def convert_image(request : Request, image: UploadFile = File(...), inputPercentage: str = Form(...)):
    temp_file = _save_file_to_disk(image, path="temp", save_as="temp")
    filename, waktu, pixel_diff = main.start(temp_file, inputPercentage)
    return ({"filename": filename, "waktu": waktu, "pixel": pixel_diff})

def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file