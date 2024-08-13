from fastapi import HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
from io import BytesIO
from handlers.withoutBackground import remove_background

MAX_FILE_SIZE_MB = 5  # Tamaño máximo de archivo en MB


async def processImage(img: UploadFile) -> BytesIO:
    try:
        # Leer el archivo de manera asíncrona
        image_data = await img.read()

        if len(image_data) > MAX_FILE_SIZE_MB * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File too large")

        image = Image.open(BytesIO(image_data))
        imgNoBg = remove_background(image)

        # Guardar la imagen procesada en un buffer
        buffered = BytesIO()
        imgNoBg.save(buffered, format="PNG")
        buffered.seek(0)

        # Limpiar recursos
        image.close()
        imgNoBg.close()

        return buffered

    except Exception as ex:
        print(f"Error processing image: {str(ex)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
