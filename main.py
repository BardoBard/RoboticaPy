import threading
from Components.Internal.Bluetooth import Bluetooth
import bluetooth

from Components.Internal.TrackMotor import TrackMotor
from Information.ControllerData import ControllerData
from Wrapper.Socket import Socket


def get_controller_data(bluetooth_socket):
    while True:
        data = bluetooth_socket.receive(14)
        ControllerData.fill_data(data)
        # TrackMotor.activate_motor()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(':)')
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    # Bluetooth.scan()

    socket = Socket(controller_mac_address)
    print(socket.address)
    print(socket.socket)
    while True:
        print(socket.receive(14))
    socket.close()
    # socket2 = Bluetooth.connect(app_mac_address, "APP") #TODO: make sure application doesn't crash

    # socket2.send("hello world")
    # Bluetooth.disconnect(socket2)

    # threading.Thread.daemon(get_controller_data(Socket))  # TODO: fix daemon thread

    # while True:
    #     print("hello")
