import cv2
import pylibdmtx.pylibdmtx as dmtx
from Components.Internal.Audio import Audio

def scan_data_matrix(frame):
    """
    :param frame: image to scan
    :return: void
    """
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    codes = dmtx.decode(gray, timeout=500)  # Set a timeout value (in milliseconds) for code detection
    
    # if codes is not empty then print the data matrix code
    if len(codes) > 0:
        # loop through all codes
        for code in codes:
            # decode the code
            data = code.data.decode('utf-8')
            print("Data Matrix Code:", data)
            # play the sound
            Audio.play_sound(Audio, "beep.wav")
