from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
from handlers.withoutBackground import noBackground
from io import BytesIO
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

proccess = APIRouter()


@proccess.post("/doc/background")
async def without_background(userId: str, img: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await img.read()))
        output_io = noBackground(image)

        output_io.seek(0)

        folder_name = os.getenv("CLOUDINARY_FOLDER_NAME_DOCS")
        file_name = f"{cloudinary.utils.random_public_id()}-{userId}"

        result = cloudinary.uploader.upload(
            output_io,
            resource_type="image",
            format="png",
            folder=folder_name,
            public_id=file_name,
        )
        url = result.get("url")
        return JSONResponse(content={"success": True, "data": url})
    except Exception as ex:
        return JSONResponse(
            content={"success": False, "error": str(ex)}, status_code=500
        )
        
@proccess.post("/payments/background")
async def without_background(userId: str, img: UploadFile = File(...)):
    try:
        image = Image.open(BytesIO(await img.read()))

        folder_name = os.getenv("CLOUDINARY_FOLDER_NAME_PAYMENT")
        file_name = f"{cloudinary.utils.random_public_id()}-{userId}"

        result = cloudinary.uploader.upload(
            image,
            resource_type="image",
            format="png",
            folder=folder_name,
            public_id=file_name,
        )
        url = result.get("url")
        return JSONResponse(content={"success": True, "data": url})
    except Exception as ex:
        return JSONResponse(
            content={"success": False, "error": str(ex)}, status_code=500
        )