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

        self.move(initial_position, speed)

    def __del__(self):
        self.move(512, 50)

    def move(self, position, speed):
        """
        moves servo to position
        @param position: position [0-1023]
        @param speed: speed [0-1023]
        @return: void
        """
        if speed <= 0:
            print("speed must be greater than zero, setting speed to 1")
            speed = 1
        try:
            ArmMotor.ax12.goto(dynamixel_id=self.__servo_id, position=position, speed=speed, degrees=False)
        except Exception:
            print("error while moving")

    # TODO: implement angle too

    @staticmethod
    def close_serial_connection():
        ArmMotor.ax12.close()
