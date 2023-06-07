import bluetooth


class Bluetooth:
    buffer_size = 1024

    @staticmethod
    def __find_index(service_matches, name):
        for i in range(len(service_matches)):
            if service_matches[i]["name"] == name:
                return i
        return 0

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
    def connect(mac_address, name=None):
        """
        connects to a given bluetooth device, using given mac address, returns socket object
        :param name:
        :param mac_address: mac address to connect
        :return: socket
        """

        # find the device using mac address
        service_matches = bluetooth.find_service(address=mac_address)

        print("found %d devices" % len(service_matches))

        # if we're unable to find the device return
        index = Bluetooth.__find_index(service_matches, name)

        # connect to mac address using socket
        try:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((mac_address, service_matches[index]["port"]))
            print("connected")
            return socket
        finally:
            if service_matches[index]["name"] is not None:
                print("name: " + service_matches[index]["name"])
            print("port: %d" % service_matches[index]["port"])
            print("protocol: " + service_matches[index]["protocol"])

        raise Exception('couldn\'t find service')

    @staticmethod
    def disconnect(socket):
        """
        disconnects from a given bluetooth device
        :param socket: socket object
        :return: void
        """
        socket.close()
