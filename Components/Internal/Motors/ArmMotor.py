class ArmMotor:
    def __init__(self, ax12, servo_id, initial_position=512, speed=50):
        """
        ctor for arm motor
        @param servo_id: servo id, between [0-253] (254 means all servos)
        @param speed: servo speed [0-1023]
        """
        self.servo_id = servo_id
        self.ax12 = ax12
        self.move(position=initial_position, speed=speed)

    # def __del__(self):
    #     self.set_speed(0)

    def move(self, position, speed):
        """
        moves servo to position
        @param position: position [0-1023]
        @param speed: speed [0-1023]
        @return: void
        """
        if speed <= 0:
            print("speed cannot be zero, setting speed to 1")
            speed = 1
        try:
            self.ax12.goto(self.servo_id, position=position, speed=speed, degrees=False)
        except Exception:
            print("something went wrong while moving")

    # TODO: implement angle too

    def close_serial_connection(self):
        self.ax12.close()
