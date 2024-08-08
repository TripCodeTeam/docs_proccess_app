import cloudinary
import cloudinary.uploader
import os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)


def uploadToCloudinary(userId: str, output_io: BytesIO, file_name: str):
    folder_name = os.getenv("CLOUDINARY_FOLDER_NAME_DOCS")
    result = cloudinary.uploader.upload(
        output_io,
        resource_type="image",
        format="png",
        folder=folder_name,
        public_id=file_name,
    )
    return result.get("url")
