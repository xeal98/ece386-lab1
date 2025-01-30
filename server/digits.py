"""
This program accepts a POST request to /predict with an image
file in the payload (payload must NOT be wrapped as a
multipart/form-data upload) and returns a JSON response
containing the inferred digit found in the image

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from tensorflow import expand_dims
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, Body
import numpy as np
from typing import List

model_path: str = "digits.keras"
dnn = load_model(model_path)

app = FastAPI()

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    img = Image.open(BytesIO(image_bytes))
    scaled = img.convert("L").resize((28, 28), resample=Image.Resampling.BICUBIC)
    return np.array(scaled, dtype=np.uint8)


@app.post("/predict/")
def predict(file: bytes = Body(media_type="application/octet-stream")):
    conv = image_to_np(file)
    result: List[np.ndarray] = dnn.predict(expand_dims(conv, 0))
    return {"digit": int(result[0].argmax())}