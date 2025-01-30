"""
This program accepts a POST request to /predict with an image
file in the payload (payload must NOT be wrapped as a
multipart/form-data upload) and returns a JSON response
containing the inferred digit found in the image

Digits.py is a FastAPI server that provides a client with an inference on
the number that is provided to the server. The number must be white on black 
in a 28x28 pixel PNG format photo. This server then returns an integer based 
on what the AI model believes it is. 

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
<<<<<<< HEAD
dnn = load_model(model_path)

app = FastAPI()
=======

# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!

digitsModel = load_model("digits.keras") #Opens the model into digitsModel

# TODO: Create FastAPI App as global variable

#serverAPI = 
>>>>>>> refs/remotes/origin/main

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    img = Image.open(BytesIO(image_bytes))
<<<<<<< HEAD
    scaled = img.convert("L").resize((28, 28), resample=Image.Resampling.BICUBIC)
    return np.array(scaled, dtype=np.uint8)
=======
    # TODO: convert image to grayscale and resize
    img = ImageOps.pad(img, (28,28), color = "#fff")
    # TODO: convert image to numpy array of shape model expects
    return None
>>>>>>> refs/remotes/origin/main


@app.post("/predict")
def predict(file: bytes = Body(media_type="application/octet-stream")):
    conv = image_to_np(file)
    result: List[np.ndarray] = dnn.predict(expand_dims(conv, 0))
    return {"digit": int(result[0].argmax())}