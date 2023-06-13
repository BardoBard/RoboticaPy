import bluetooth

from Components.Internal.Bluetooth import Bluetooth


class Socket:
    # socket  <- this being used as non-static variable
    # address <- this being used as non-static variable
    # name    <- this being used as non-static variable

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
        return Bluetooth.check_connection(self.socket)
    
    def __reconnect_if_needed(self):
        if self.check_connection():
            return
        
        self.socket = Bluetooth.connect(self.address, self.name)
    
    # def check_connection(self):
    #     """
    #     checks connection, keeps trying until connection is established
    #     :return: new connection socket
    #     """
    #     socket_value = object.__getattribute__(self, '__dict__').get('socket')
    #     if not Bluetooth.check_connection(socket_value):
    #         print("connection lost, trying to reconnect")
    #         socket_value = Bluetooth.connect(self.address, self.name)
    #     return socket_value

    # def __getattribute__(self, name):
    #     if name == 'socket':
    #         self.socket = self.check_connection()
    #     return super().__getattribute__(name)

    def __del__(self):
        """
        dtor, closes connection
        :return: void
        """
        self.close()

    def send(self, message):
        """
        sends bytes via bluetooth connection
        :param message: byte array
        :return: void
        """
        self.__reconnect_if_needed()
        
        try:
            self.socket.send(message)
        except Exception:
            print('error while sending')

    def receive(self, size):
        """
        receives connection, returns a byte array of size
        :param size: of byte array
        :return: byte array
        """
        self.__reconnect_if_needed()
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
        try:
            self.socket.close()
        except Exception:
            print('error closing, maybe the connection went out of range')
