import bluetooth

from Components.Internal.Bluetooth import Bluetooth


class Socket:
    socket = None
    address = None
    name = None

    def __init__(self, address, name=None):
        """
        ctor
        :param address: mac address
        :param name: name of the bluetooth socket
        """
        self.address = address
        self.name = name
        self.socket = Bluetooth.connect(address, name)

    def check_connection(self):
        """
        checks connection, keeps trying until connection is established
        :return: new connection socket
        """
        socket_value = object.__getattribute__(self, '__dict__').get('socket')
        while not Bluetooth.check_connection(socket_value):
            print("connection lost, reconnecting soon...")
            socket_value = Bluetooth.connect(self.address, self.name)
        return socket_value

    def __getattribute__(self, name):
        if name == 'socket':
            self.socket = self.check_connection()
        return super().__getattribute__(name)

    def __del__(self):
        """
        dtor, closes connection
        :return: void
        """
        self._socket.close()

    def send(self, message):
        """
        sends bytes via bluetooth connection
        :param message: byte array
        :return: void
        """
        try:
            self._socket.send(message)
        except Exception:
            print('error while sending')

    def receive(self, size):
        """
        receives connection, returns a byte array of size
        :param size: of byte array
        :return: byte array
        """
        try:
            return self.socket.recv(size)
        except Exception:
            print('error while receiving')
        return None

    def close(self):
        """
        closes socket connection
        :return: void
        """
        self.socket.close()
