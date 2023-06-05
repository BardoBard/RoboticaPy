import bluetooth


class Bluetooth:
    buffer_size = 1024

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
    def connect(mac_address):
        """
        connects to a given bluetooth device, using given mac address, returns socket object
        :param mac_address: mac address to connect
        :return: socket
        """

        # find the device using mac address
        service_matches = bluetooth.find_service(address=mac_address)

        # if we're unable to find the device return
        if len(service_matches) == 0:
            print("no services found")
            return None

        # if there is only one device with the mac address connect using socket
        if len(service_matches) == 1:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((mac_address, service_matches[0]["port"]))
            return socket

        return None

    @staticmethod
    def disconnect(socket):
        """
        disconnects from a given bluetooth device
        :param socket: socket object
        :return: void
        """
        socket.close()
