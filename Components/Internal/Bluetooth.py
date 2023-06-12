import bluetooth


class Bluetooth:
    @staticmethod
    def scan():
        """
        scans the bluetooth devices and prints them
        :return: void
        """
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("found %d devices" % len(nearby_devices))

        for addr, name in nearby_devices:
            print(" %s - %s" % (addr, name))

    @staticmethod
    def connect(mac_address, name=None):  # TODO: bluetooth.find_service can have a name
        """
        connects to a given bluetooth device, using given mac address, returns socket object
        :param name:
        :param mac_address: mac address to connect
        :return: socket
        """

        # find the device using mac address
        services = bluetooth.find_service(address=mac_address,
                                                 name=name)  # TODO: this is slow, due to a timeout that cannot be changed

        # If we're unable to find the device, return None
        if not services and len(services) != 1:
            print(f"{len(services)} services found, expecting : 1")
            return None

        service = services[0]

        # connect to mac address using socket
        try:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((mac_address, service["port"]))
            print("connected")
            socket.settimeout(0.5)
            return socket

        except Exception as e:
            if service["name"] is not None:
                print("name: " + service["name"])
            print("port: %d" % service["port"])
            print("protocol: " + service["protocol"])
            print(e)

    @staticmethod
    def check_connection(socket):
        """
        check connection between socket and server
        :param socket: socket object
        :return: true if connection is still alive
        """
        try:
            socket.recv(0)
            return True
        except Exception:
            print("bluetooth connection disconnected")
            return False

    @staticmethod
    def disconnect(socket):
        """
        disconnects from a given bluetooth device
        :param socket: socket object
        :return: void
        """
        socket.close()
