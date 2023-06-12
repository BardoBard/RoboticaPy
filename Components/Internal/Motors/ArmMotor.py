import RPi.GPIO as GPIO

from Packages.Ax12 import Ax12


class ArmMotor:
    conditional_pin = 18  # this is a static variable, python doesn't have a keyword for it :D

    # my_dxl <- non static variable

    Ax12.DEVICENAME = '/dev/ttyS0'  # this is the port for the servo
    Ax12.BAUDRATE = 1_000_000
    Ax12.connect()

    # pin setup
    GPIO.setwarnings(False)  # suppress warning if gpio pin hasn't been properly configured
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(conditional_pin, GPIO.OUT)
    print("")

    def __init__(self, servo_id, speed):
        """
        ctor for arm motor
        @param servo_id: servo id, between [0-253] (254 means all servos)
        @param speed: servo speed [0-1023]
        """
        self.my_dxl = Ax12(servo_id)
        self.set_speed(speed)

    def move(self, position):
        """
        moves servo to position
        @param position: position [0-1023]
        @return: void
        """
        GPIO.output(ArmMotor.conditional_pin, GPIO.HIGH)
        self.my_dxl.set_goal_position(position)

    def set_speed(self, speed):
        """
        sets the speed of the servo
        @param speed: int between [0-1023]
        @return: void
        """
        self.my_dxl.set_moving_speed(speed)

    def disconnect(self):
        """
        disconnects the servo
        @return: void
        """
        self.my_dxl.set_torque_enable(0)
        Ax12.disconnect()
