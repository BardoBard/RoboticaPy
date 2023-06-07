import time

from Components.Internal.Bluetooth import Bluetooth


class Socket:
    _socket = None
    _address = None
    _name = None

    def __getattribute__(self, name):
        if name == '_socket':
            print('socket')
            self.check_connection()  # Check the connection before accessing _socket

    def check_connection(self):
        while self._socket is None:
            print("connection lost, reconnecting in 1 second")
            time.sleep(1)
            self._socket = Bluetooth.connect(self._address, self._name)

    def __init__(self, address, name=None):
        self._address = address
        self._name = name
        self._socket = Bluetooth.connect(address, name)

    # def __del__(self):
    #     self._socket.close()

    def send(self, message):
        print("printing socket...")
        print(self._socket)
        self._socket.send(message)

    def receive(self, size):
        self._socket.recv(size)

    def close(self, size):
        self._socket.close()
