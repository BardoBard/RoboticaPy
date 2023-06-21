from pyax12.connection import Connection
import time

from Components.Internal.Motors import ArmMotor

ax12 = Connection(port="/dev/ttyS0", baudrate=1_000_000)


class Dance:
    def __init__(self):
        pass

    def do_dance(self):
        ax12.goto(7, position=612, speed=20, degrees=False)
        ax12.goto(3, position=412, speed=20, degrees=False)

        time.sleep(10)

        ax12.goto(7, position=412, speed=20, degrees=False)
        ax12.goto(3, position=612, speed=20, degrees=False)

        # wait
        # turnaround

        # 15 rotatatie
        # 7 links 3 rechts bovenarm
        # 4 links 10 rechts
        # 5 grabby
        return
