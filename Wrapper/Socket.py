import time
import bluetooth

from Components.Internal.Bluetooth import Bluetooth


class Socket:
    socket = None
    address = None
    name = None

    def __init__(self, address, name=None):
        self.address = address
        self.name = name
        self.socket = Bluetooth.connect(address, name)
        print(self.socket is None)

    def check_connection(self):
        while self.socket is None:
            print("connection lost, reconnecting in 1 second")
            time.sleep(1)
            self.socket = Bluetooth.connect(self.address, self.name)

    def __getattribute__(self, name):
        if name == 'socket':
            print('socket')
            self.check_connection()

    # def __del__(self):
    #     self._socket.close()

    def send(self, message):
        print("printing socket...")
        print(self.socket)
        # self._socket.send(message)

    def receive(self, size):
        self.socket.recv(size)

    def close(self, size):
        self.socket.close()
