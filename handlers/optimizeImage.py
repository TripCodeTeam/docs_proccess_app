import cv2
import numpy as np
from PIL import Image


def optimizeImage(image: Image) -> Image:
    # Convertir la imagen a un formato que OpenCV pueda manejar
    open_cv_image = np.array(image.convert("RGB"))
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)

    # Redimensionar la imagen si es demasiado grande (puedes ajustar los valores según tus necesidades)
    height, width, _ = open_cv_image.shape
    max_dimension = 1024  # Tamaño máximo de dimensión (ancho o alto)
    if max(height, width) > max_dimension:
        scaling_factor = max_dimension / max(height, width)
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        open_cv_image = cv2.resize(
            open_cv_image, (new_width, new_height), interpolation=cv2.INTER_AREA
        )

    # Convertir de nuevo a imagen PIL
    result_rgb = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)
    optimized_image = Image.fromarray(result_rgb)

    return optimized_image
