import time

import RPi.GPIO as GPIO
import serial
from pyax12 import connection
import dynamixel_sdk

# from Components.Internal.Motors.Ax12 import Ax12


class ArmMotor:
    @staticmethod
    def initialize():
        # Ax12.DEVICENAME = '/dev/ttyAMA0'
        # Ax12.BAUDRATE = 1_000_000

        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(18, GPIO.OUT)
        # GPIO.output(18, GPIO.HIGH)

        port = "/dev/ttyAMA0"
        baudrate = 1000000
        servo_id = 254

        ax12 = connection.Connection(port=port, baudrate=baudrate)

        ax12.set_goal_position(servo_id, 512)

        time.sleep(2)

        ax12.close()
