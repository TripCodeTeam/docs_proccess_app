from fastapi import HTTPException, UploadFile
from PIL import Image
from io import BytesIO

# from handlers.compres import compressImage
from handlers.uploadCloudinary import uploadToCloudinary
from handlers.withoutBackground import remove_background

MAX_FILE_SIZE_MB = 5  # Tamaño máximo de archivo en MB


async def processImage(userId: str, img: UploadFile, type: str):
    try:
        # Leer el archivo de manera asíncrona
        image_data = await img.read()

        if len(image_data) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File too large")

        image = Image.open(BytesIO(image_data))
        imgNoBg = remove_background(image)

        # Subir a Cloudinary
        file_name = f"{type}-{userId}"
        url = uploadToCloudinary(userId, imgNoBg, file_name)

        return url

    except Exception as ex:
        print(f"Error processing image: {str(ex)}")
