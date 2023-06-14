from pyax12.connection import Connection


class ArmMotor:
    ax12 = Connection(port="/dev/ttyS0", baudrate=1_000_000, rpi_gpio=True)

    def __init__(self, servo_id, speed=0):
        """
        ctor for arm motor
        @param servo_id: servo id, between [0-253] (254 means all servos)
        @param speed: servo speed [0-1023]
        """
        self.servo_id = servo_id
        self.speed = speed

        self.set_speed(speed)

    def __del__(self):
        self.set_speed(0)

    def move(self, position):
        """
        moves servo to position
        @param position: position [0-1023]
        @return: void
        """
        ArmMotor.ax12.goto(self.servo_id, position, self.speed, degrees=False)

    # TODO: implement angle too

    def set_speed(self, speed):
        """
        sets the speed of the servo
        important: 1023 is 114 RPM! 300 means 33 RPM
        @param speed: int between [0-1023]
        @return: void
        """
        self.ax12.set_speed(self.servo_id, speed)

    def disconnect(self):
        """
        disconnects the servo
        @return: void
        """
        self.set_speed(0)

    @staticmethod
    def close_serial_connection():
        ArmMotor.ax12.close()
