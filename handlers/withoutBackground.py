from rembg import remove
from PIL import Image
from io import BytesIO
from handlers.optimizeImage import optimizeImage


def remove_background(img: Image) -> BytesIO:
    # Optimizar la imagen antes de eliminar el fondo
    optimized_image = optimizeImage(img)
    output = remove(optimized_image)
    output_io = BytesIO()
    output.save(output_io, format="PNG")
    output_io.seek(0)
    return output_io
