import RPi.GPIO as GPIO

from Packages.Ax12 import Ax12


class ArmMotor:
    conditional_pin = 18  # this is a static variable, python doesn't have a keyword for it :D

    # my_dxl <- non static variable
    Ax12.DEVICENAME = '/dev/ttyS0'  # this is the port for the servo
    Ax12.BAUDRATE = 1_000_000

    # pin setup
    GPIO.setwarnings(False)  # suppress warning if gpio pin hasn't been properly configured
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(conditional_pin, GPIO.OUT)

    def __init__(self, servo_id, speed=0, cw_angle=0, ccw_angle=1023, enable_torque=True, torque=1023):
        """
        ctor for arm motor
        @param servo_id: servo id, between [0-253] (254 means all servos)
        @param speed: servo speed [0-1023]
        """
        Ax12.connect()
        self.my_dxl = Ax12(servo_id)
        self.set_speed(speed)

        self.set_torque(torque)
        self.enable_torque(enable_torque)

        self.cw_angle_limit(cw_angle)
        self.ccw_angle_limit(ccw_angle)

   # def __del__(self):
    #    self.disconnect()

    def move(self, position):
        """
        moves servo to position
        @param position: position [0-1023]
        @return: void
        """
        GPIO.output(ArmMotor.conditional_pin, GPIO.HIGH)
        self.my_dxl.set_goal_position(position)

    # TODO: implement angle instead of position

    def set_speed(self, speed):
        """
        sets the speed of the servo
        important: 1023 is 114 RPM! 300 means 33 RPM
        @param speed: int between [0-1023]
        @return: void
        """
        self.my_dxl.set_moving_speed(speed)

    def enable_torque(self, torque_bool):
        self.my_dxl.set_torque_enable(torque_bool)

    def set_torque(self, torque):
        self.my_dxl.set_max_torque(torque)

    def ccw_angle_limit(self, limit):
        self.my_dxl.set_ccw_angle_limit(limit)

    def cw_angle_limit(self, limit):
        self.my_dxl.set_ccw_angle_limit(limit)

    def disconnect(self):
        """
        disconnects the servo
        @return: void
        """
        self.enable_torque(False)
        self.set_torque(0)
        self.set_speed(0)
        self.my_dxl.disconnect()
