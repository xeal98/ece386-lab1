"""
TODO: Insert what this program does here.
"""

import sys
import requests


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    # print(f"http://{server_ip}:{server_port}{api_path}") #Used for testing to make sure the string was being made the desired way

    file = open(image_path, "br")
    postInfo = requests.post(
        f"http://{server_ip}:{server_port}{api_path}",
        data=bytes(file.read()),
        timeout=2,
    )
    # getInfo = requests.get(f"http://{server_ip}:{server_port}", timeout=2)
    # getInfo.raise_for_status()
    postInfo.raise_for_status()
    # decodedGetJSON = getInfo.json()
    decodedPostJSON = postInfo.json()
    return decodedPostJSON
    # return decodedGetJSON


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    print(f"Using server {server_ip}:{server_port}")
    while True:
        filePath = input("Enter the file path of the digit to be identified: ")
        serverPrediction = get_img_prediction(
            server_ip, server_port, "/predict", filePath
        )
        print(serverPrediction)


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
