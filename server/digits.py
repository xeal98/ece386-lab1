"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, File, UploadFile
import numpy as np
from typing import Annotated

model_path: str = "digits.keras"
dnn = load_model(model_path)

app = FastAPI()


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    img = Image.open(BytesIO(image_bytes))
    scaled = img.convert("L").resize((28, 28), resample=Image.Resampling.BICUBIC)
    return np.array(scaled, dtype=np.uint8)


@app.post("/predict")
async def predict(file: Annotated[int, File()]):
    return {"digit": dnn.predict(image_to_np(file))}
    # return {"file_size": len(file)}
