from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from handlers.processImg import processImage

load_dotenv()


proccess = APIRouter()


@proccess.post("/doc/background")
async def without_background(
    userId: str = Form(...),
    img: UploadFile = File(...),
    type: str = Form(...),
):
    try:
        url = await processImage(userId, img, type)

        if url:
            return JSONResponse(content={"success": True, "data": url})
        else:
            return JSONResponse(
                content={"success": False, "error": "Failed to process image"},
                status_code=500,
            )
    except Exception as ex:
        return JSONResponse(
            content={"success": False, "error": str(ex)}, status_code=500
        )
