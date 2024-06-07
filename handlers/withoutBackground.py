from rembg import remove
from PIL import Image
from io import BytesIO


def noBackground(img: Image) -> BytesIO:
    output = remove(img)
    output_io = BytesIO()
    output.save(output_io, format="PNG")
    output_io.seek(0)
    return output_io
