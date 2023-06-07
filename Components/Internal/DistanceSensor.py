import RPi.GPIO as GPIO  # does not work on windows must be installed on pi
from gpiozero import DistanceSensor as DS
import time


class DistanceSensor:

    sensor = DS(23,24) #random pins need to be changed later

    def find_distance(self):
        a = DS.sensor.distance
        return
