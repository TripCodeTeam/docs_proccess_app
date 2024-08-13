from rembg import remove
from PIL import Image
from io import BytesIO


def remove_background(img: Image) -> BytesIO:
    try:
        # Optimizar la imagen antes de eliminar el fondo
        output = remove(img)

        output_io = BytesIO()
        output.save(output_io, format="PNG")
        output_io.seek(0)

        output_image = Image.open(output_io)

        return output_image
    except Exception as ex:
        print(f"Error removing background: {str(ex)}")
        raise
