import asyncio
import threading
from Components.Internal.Bluetooth import Bluetooth
import bluetooth

from Components.Internal.TrackMotor import TrackMotor
from Information.ControllerData import ControllerData
from Wrapper.Socket import Socket


def get_controller_data(bluetooth_socket):
    while True:
        print("printing")
        data = bluetooth_socket.receive(14)
        ControllerData.fill_data(data)
        TrackMotor.activate_motor()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(':)')
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address

    socket = Socket(controller_mac_address)
    socket_app = Socket(app_mac_address)
    get_controller_data(socket)
