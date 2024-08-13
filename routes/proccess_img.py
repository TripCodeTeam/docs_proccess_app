from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from dotenv import load_dotenv
from handlers.processImg import processImage

load_dotenv()


proccess = APIRouter()


@proccess.post("/doc/background")
async def without_background(img: UploadFile = File(...)):
    try:
        image_buffer = await processImage(img)

        if image_buffer:
            return StreamingResponse(
                image_buffer,
                media_type="image/png",
                headers={
                    "Content-Disposition": "attachment; filename=processed_image.png"
                },
            )
        else:
            return JSONResponse(
                content={"success": False, "error": "Failed to process image"},
                status_code=500,
            )
    except Exception as ex:
        return JSONResponse(
            content={"success": False, "error": str(ex)}, status_code=500
        )
