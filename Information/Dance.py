from pyax12.connection import Connection
import time

from Components.Internal.Motors.TrackMotor import TrackMotor

ax12 = Connection(port="/dev/ttyS0", baudrate=1_000_000)


class Dance:
    def __init__(self):
        pass

    def do_dance(self):
        tracks = TrackMotor()
        #never going to give you up
        ax12.goto(3, position=612, speed=20, degrees=False)
        ax12.goto(7, position=412, speed=20, degrees=False)

        time.sleep(2)

        #never going to let you down
        ax12.goto(3, position=412, speed=20, degrees=False)
        ax12.goto(7, position=612, speed=20, degrees=False)

        time.sleep(2)

        #Never gonna run around and desert you
        tracks.move(30,-30)
        time.sleep(2)
        tracks.move(0,0)
        # turnaround

        #Never gonna make you cry
        #eyes?
        time.sleep(2)
        #Never gonna say goodbye
        ax12.goto(15, position=412, speed=20, degrees=False)
        time.sleep(2)
        #Never gonna tell a lie and hurt you
        ax12.goto(15, position=612, speed=20, degrees=False)

        # 15 rotatatie
        # 7 links 3 rechts bovenarm
        # 4 links 10 rechts
        # 5 grabby
        return
