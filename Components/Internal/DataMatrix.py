import cv2
import pylibdmtx.pylibdmtx as dmtx


def scan_data_matrix(image_data):
    """
    :param image_data: ImageData
    :return: ImageData
    """
    # convert to grayscale
    gray = cv2.cvtColor(image_data.image, cv2.COLOR_BGR2GRAY)
    codes = dmtx.decode(
        gray, timeout=50
    )  # Set a timeout value (in milliseconds) for code detection

    # if codes is not empty then print the data matrix code
    if len(codes) <= 0:
        return

    decoded_codes = []

    # loop through all codes
    for code in codes:
        # decode the code
        data = code.data.decode("utf-8")
        # add the code to the list
        decoded_codes.append(data)

    # add the codes to the image data
    image_data.matrix_code = decoded_codes
    return image_data
