import time

import RPi.GPIO as GPIO
import serial
import dynamixel_sdk

from Components.Internal.Motors.Ax12 import Ax12


class ArmMotor:
    my_dxl = None

    def __init__(self):
        Ax12.DEVICENAME = '/dev/ttyS0'
        Ax12.BAUDRATE = 1_000_000

        Ax12.connect()

        self.my_dxl = Ax12(254)
        self.my_dxl.set_moving_speed(200)

        GPIO.cleanup()

        GPIO.setmode(GPIO.BCM)

        # if GPIO.gpio_function(18) != GPIO.OUT:
        GPIO.setup(18, GPIO.OUT)

        GPIO.output(18, GPIO.HIGH)

    def move(self, value):
        self.my_dxl.set_goal_position(value)

    def disconnect(self):
        self.my_dxl.set_torque_enable(0)
        Ax12.disconnect()
