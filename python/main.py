import os
import logging
import pathlib
from fastapi import FastAPI, Form, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import item_service
import helpers

app = FastAPI()
logger = logging.getLogger("uvicorn")
logger.level = logging.INFO
images = pathlib.Path(__file__).parent.resolve() / "image"
origins = [ os.environ.get('FRONT_URL', 'http://localhost:3000') ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return item_service.get_all_items()

@app.post("/items")
async def add_item(name: str = Form(...), category_id: int = Form(...), image: UploadFile | None = None):
    logger.info(f"Receive item: {name}, category_id: {category_id}")

    if not image:
        return item_service.insert_item(name, category_id, None)

    hashed_file_name = helpers.hash_image(image.filename)
    file_path = images / hashed_file_name
    file_upload_result = await helpers.upload_image(file_path, image)
    
    return item_service.insert_item(name, category_id, file_upload_result)

@app.get("/search")
def search_items(keyword: str):
    return item_service.search_item(keyword)

@app.get("/image/{items_image}")
async def get_image(items_image):
    # Create image path
    image = images / items_image

    if not items_image.endswith(".jpg"):
        raise HTTPException(status_code=400, detail="Image path does not end with .jpg")

    if not image.exists():
        logger.debug(f"Image not found: {image}")
        image = images / "default.jpg"

    return FileResponse(image)

@app.get("/items/{item_id}")
def get_item(item_id):
    return item_service.get_item(item_id)