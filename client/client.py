"""
This program allows for the remote connection to a server hosting an AI model
that is able to predict digits, given that they are white on a black background.
Additionally, the images must be in a 28x28 pixel file with a PNG format.

It does this through a POST request to the server with the API path hard set to
'/predict' because that is the only function that the server can provide. It then 
sends a binary stream to the server where it is then rebuilt into the image. The 
server will then respond with the digit that it believes it is.
"""

import sys
import requests
from json import loads as parse


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    file = open(image_path, "br")
    headers = {"Content-Type": "application/octet-stream"}
    postInfo = requests.post(
        f"http://{server_ip}:{server_port}{api_path}",
        headers=headers,
        data=bytes(file.read()),
        timeout=2,
    )
    postInfo.raise_for_status()
    return postInfo.text


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    print(f"Using server {server_ip}:{server_port}")
    while True:
        filePath = input("Enter the file path of the digit to be identified: ")
        serverPrediction = get_img_prediction(
            server_ip, server_port, "/predict", filePath
        )
        decoded = parse(serverPrediction)
        print("Predicted digit: " + str(decoded["digit"]))


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
