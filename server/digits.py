"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

Digits.py is a FastAPI server that provides a client with an inference on
the number that is provided to the server. The number must be white on black 
in a 28x28 pixel PNG format photo. This server then returns an integer based 
on what the AI model believes it is. 

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO

model_path: str = "digits.keras"

# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!

digitsModel = load_model("digits.keras") #Opens the model into digitsModel

# TODO: Create FastAPI App as global variable

#serverAPI = 

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    img = ImageOps.pad(img, (28,28), color = "#fff")
    # TODO: convert image to numpy array of shape model expects
    return None


# TODO: Define predict POST function
