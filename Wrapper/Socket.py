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

    def check_connection(self):
        socket_value = object.__getattribute__(self, '__dict__').get('socket')
        while not Bluetooth.check_connection(socket_value):
            print("connection lost, reconnecting in 1 second")
            time.sleep(1)
            socket_value = Bluetooth.connect(self.address, self.name)
        return socket_value

    # here is the error
    def __getattribute__(self, name):
        if name == 'socket':
            print('socket')
            self.socket = self.check_connection()
        return super().__getattribute__(name)  # Fall back to default behavior

    # def __del__(self):
    #     self._socket.close()

    def send(self, message):
        try:
            self._socket.send(message)
        except Exception:
            print('Error')

    def receive(self, size):
        try:
            return self.socket.recv(size)
        except Exception:
            print('Error')

    def close(self):
        self.socket.close()
