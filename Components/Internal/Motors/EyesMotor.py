import pigpio


class EyesMotor:
    """
    class for micro servo 9G SG90
    """

    @staticmethod
    def turn():
        pigpio.pi()
