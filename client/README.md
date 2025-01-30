# Digits Client

The client is able to communicate with a server that is able to make predictions on an image, assuming that the API path is /predict. This enables the user to be 

## Usage

Upload the images that you want to run against the model saved on the server into this folder, or the *img* folder

1. Create a virtual python environment in this folder. 
2. Make sure to access that virtual environment for step 3
3. Run ```pip install -r requirements.txt```
4. Then run ```python3 client.py <ipaddress> <port>```

It will then prompt you for the address in the file system for the image that you want to be predicted on the server running the model. It will continue to do so until you press Ctrl+C to exit, or really any keyboard interrupt. 

You are now ready to start predicting!