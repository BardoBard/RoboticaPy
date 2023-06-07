import time

from Components.Internal.Bluetooth import Bluetooth


class Socket:
    __socket = False
    __address = None
    __name = None

    def __getattribute__(self, name):
        if name == '_socket':
            print('socket')
            self.check_connection()  # Check the connection before accessing _socket

    def check_connection(self):
        while self.__socket is None:
            print("connection lost, reconnecting in 1 second")
            time.sleep(1)
            self.__socket = Bluetooth.connect(self._address, self._name)

    def __init__(self, address: str, name: str = None):
        self._address = address
        self._name = name
        self.__socket = Bluetooth.connect(address, name)
        print(self.__socket is None)

    # def __del__(self):
    #     self._socket.close()

    def send(self, message):
        print("printing socket...")
        print(self.__socket)
        # self._socket.send(message)

    def receive(self, size):
        self.__socket.recv(size)

    def close(self, size):
        self.__socket.close()
