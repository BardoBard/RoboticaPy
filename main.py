import time
from Components.Internal.Bluetooth import Bluetooth
import bluetooth
from Information.ControllerData import ControllerData


def get_controller_data(socket):
    while True:
        time.sleep(0.1)
        data = socket.recv(Bluetooth.buffer_size)
        ControllerData.fill_data(data)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(':)')
    controller_mac_address = "78:21:84:7C:A4:F6" #controller_mac_address
    # controller_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    # Bluetooth.scan()

    socket = Bluetooth.connect(controller_mac_address, "APP")
    Bluetooth.disconnect(socket)
    t1 = threading.Thread(get_controller_data())
    t1.start()
    print("hello")
    t1.join()
