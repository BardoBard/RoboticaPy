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
        """Checks if the connection is still valid

        Returns:
            Bool: False if invalid, True if valid
        """
        return Bluetooth.check_connection(self.socket)
    
    def __reconnect_if_needed(self):
        """Checks if there is a valid connection 
        and automatically attempts to reconnect if there isn't
        """
        if self.check_connection():
            return
        
        self.socket = Bluetooth.connect(self.address, self.name)

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
