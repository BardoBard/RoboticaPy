import RPi.GPIO as GPIO
import pyax12.packet
import serial
from pyax12 import packet
from pyax12 import connection


class ArmMotor:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)

    @staticmethod
    def initialize():
        servo_id = 254
        serial_connection = connection.Connection(port="/dev/ttyUSB0", baudrate=1000000, timeout=3.0)
        print("scanning...")

        serial_connection.goto(servo_id, 512, speed=200, degrees=True)

        print("closing")
        serial_connection.close()
