import time

import RPi.GPIO as GPIO
import serial
from pyax12 import connection
import dynamixel_sdk

from Components.Internal.Motors.Ax12 import Ax12


class ArmMotor:
    @staticmethod
    def initialize():
        Ax12.DEVICENAME = '/dev/ttyAMA0'
        Ax12.BAUDRATE = 1_000_000

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        Ax12.connect()
        my_dxl = Ax12(254)
        my_dxl.set_moving_speed(200)

        my_dxl.set_goal_position(500)

        my_dxl.set_torque_enable(0)
        Ax12.disconnect()
