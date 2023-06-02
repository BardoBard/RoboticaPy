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

    def main(self):
        # main loop or what/however is done because i don't know how constructer/ destructors work at the moment in
        # python im doing camera stuff in this loop as well
        opencv_ = OpenCv()
        cap = cv2.VideoCapture(0)
        while 1:
            ret, img = cap.read()
            if ret:
                opencv_.detect_object(img)

                if cv2.waitKey(5) >= 0:
                    break

            else:  # empty image
                break

        return
