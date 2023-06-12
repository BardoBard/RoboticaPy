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
        packet_handler = packet.PACKET_HEADER()
        serial_connection = connection.Connection(port="/dev/ttyAMA0", baudrate=1000000, timeout=3.0)
        print("scanning...")

        packet_handler.torque_enable(servo_id, True)

        packet_handler.set_goal_position(servo_id, 512)

        packet_handler.set_moving_speed(servo_id, 200)

        print("closing")
        serial_connection.close()
