import RPi.GPIO as GPIO
import serial
from pyax12 import connection


class ArmMotor:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)

    @staticmethod
    def initialize():
        serial_connection = serial.Serial(port="/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
        print("scanning...")
        # ids_available = serial_connection.scan()

        # for dynamixel_id in ids_available:
        #     print(dynamixel_id)

        serial_connection.write(bytearray.fromhex("FF FF 01 05 03 1E 32 03 A3"))

        # serial_connection.goto(254, 45, speed=200, degrees=True)

        print("closing")
        serial_connection.close()
