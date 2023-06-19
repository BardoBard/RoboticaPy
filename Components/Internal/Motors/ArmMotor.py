from pyax12.connection import Connection


class ArmMotor:
    ax12 = Connection(port="/dev/ttyS0", baudrate=1_000_000, rpi_gpio=True)

    def __init__(self, servo_id, speed=50, initial_position=512):
        """
        ctor for arm motor
        @param servo_id: servo id, between [0-253] (254 means all servos)
        @param speed: servo speed [0-1023]
        """
        self.__servo_id = servo_id
        self.__speed = speed

        self.set_speed(speed)
        self.move(initial_position)

    def __del__(self):
        self.set_speed(50)
        self.move(512)

    def move(self, position):
        """
        moves servo to position
        @param position: position [0-1023]
        @return: void
        """
        try:
            ArmMotor.ax12.goto(self.__servo_id, position, self.__speed, degrees=False)
        except Exception:
            print("error while moving")

    # TODO: implement angle too

    def set_speed(self, speed):
        """
        sets the speed of the servo
        important: 1023 is 114 RPM! 300 means 33 RPM
        @param speed: int between [1-1023]
        @return: void
        """
        if speed <= 0:
            speed = 1
            print("error setting speed, too low: " + str(speed))

        self.__speed = speed

        try:
            self.ax12.set_speed(self.__servo_id, speed)
        except Exception:
            print("error setting speed")

    @staticmethod
    def close_serial_connection():
        ArmMotor.ax12.close()
