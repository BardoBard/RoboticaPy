import threading
import time
from Components.Internal.Bluetooth import Bluetooth
import bluetooth

from Components.Internal.TrackMotor import TrackMotor
from Information.ControllerData import ControllerData


def get_controller_data(socket):
    while True:
        time.sleep(0.5)
        data = socket.recv(Bluetooth.buffer_size)
        ControllerData.fill_data(data)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(':)')
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    # Bluetooth.scan()

    TrackMotor.activate_motor()

    # socket = Bluetooth.connect(controller_mac_address)
    # socket2 = Bluetooth.connect(app_mac_address, "APP") #TODO: make sure application doesn't crash

    # socket2.send("hello world")
    # Bluetooth.disconnect(socket2)

    # threading.Thread.daemon(get_controller_data(socket))  # TODO: fix daemon thread

    # while True:
    #     print("hello")
