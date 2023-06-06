import cv2
import numpy as np

from Components.Internal.OpenCv import OpenCv


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
            ret, img = cap.read()
            if ret:
                cv2.imshow('picture', opencv_.detect_object(img).image) #todo remove for pi

                if cv2.waitKey(5) >= 0:
                    break

            else:  # empty image
                break
