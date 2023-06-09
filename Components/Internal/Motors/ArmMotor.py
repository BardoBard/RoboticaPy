from pyax12 import *
import pigpio


class ArmMotor:
    pi = pigpio.pi()

    @staticmethod
    def initialize():
        ArmMotor.pi.set_mode(18, pigpio.OUTPUT)
        ArmMotor.pi.write(18, pigpio.HIGH)
        serial_connection = connection.Connection(port="/dev/tty0", baudrate=1000000)
        ids_available = serial_connection.scan()

        for dynamixel_id in ids_available:
            print(dynamixel_id)

            serial_connection.goto(dynamixel_id, 45, speed=200, degrees=True)

        print("closing")
        serial_connection.close()
