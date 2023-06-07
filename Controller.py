import cv2
import numpy as np
import asyncio

from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix


class Controller:
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
                img2 = opencv_.detect_object(img, 1000)
                cv2.imshow('picture', img2.image) #todo remove for pi
                # if the image found a box (imageData.found == true) then scan the data matrix
                if img2.found:
                    # scan the data matrix code
                    asyncio.run(scan_data_matrix(img2.image))

                if cv2.waitKey(5) >= 0:
                    break

            else:  # empty image
                break
