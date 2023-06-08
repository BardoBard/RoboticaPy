import cv2
import numpy as np
import asyncio

from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix


class Controller:
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    app_service_name = "APP"
    
    def remote_to_arm(self, value):
        return  # void

    def weight_to_text(self, weight):  # not sure what this does, perhaps not necessary
        return  # void

    def turn_led_on(self, frequency):
        return  # void

    def detect_object(self):  # maybe needs to be removed
        return  # void

    if __name__ == '__main__':
        # main loop

        opencv_ = OpenCv()
        cap = cv2.VideoCapture(0)
        while 1:
            # get the image
            ret, img = cap.read()
            # if the image is not empty
            if ret:
                # detect the object
                image_data = opencv_.detect_object(img, 1000)
                # if the image found a box (imageData.found == true) then scan the data matrix
                if image_data.found:
                    # scan the data matrix code
                    scan_data_matrix(image_data)
                    image_data.print_to_command_line()

                if cv2.waitKey(5) >= 0:
                    break

            else:  # empty image
                break
    
