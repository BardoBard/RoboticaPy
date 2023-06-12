import time

import RPi.GPIO as GPIO
import serial
from pyax12 import connection


class ArmMotor:
    @staticmethod
    def initialize():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)

        servo_id = 254
        # serial_connection = connection.Connection(port="/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
        port = serial.Serial(port="/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
        print("scanning...")

        while True:
            time.sleep(3)
            port.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 Fb"))
            time.sleep(3)
            port.write(bytearray.fromhex("FF FF 01 05 03 1E CD 00 0b"))
        # serial_connection.goto(servo_id, 45, speed=200, degrees=True)

        print("closing")
        # serial_connection.close()
