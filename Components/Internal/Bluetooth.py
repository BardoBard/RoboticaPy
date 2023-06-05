import bluetooth


class Bluetooth:
    buffer_size = 1024

    @staticmethod
    def __find_index(service_matches, name):
        for i in range(len(service_matches)):
            if service_matches[i]["name"] == name:
                return i
        raise Exception('couldn\'t find service')

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
    def connect(mac_address, name):
        """
        connects to a given bluetooth device, using given mac address, returns socket object
        :param name:
        :param mac_address: mac address to connect
        :return: socket
        """

        # find the device using mac address
        service_matches = bluetooth.find_service(address=mac_address)

        print("found %d devices" % len(service_matches))

        for i in range(len(service_matches)):
            if service_matches[i]["name"] is not None:
                print("name: " + service_matches[i]["name"])
            print("port: %d" % service_matches[i]["port"])
            print("protocol: " + service_matches[i]["protocol"])

        # if we're unable to find the device return
        index = Bluetooth.__find_index(service_matches, name)

        # if there is only one device with the mac address connect using socket
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((mac_address, service_matches[index]["port"]))
        return socket

    @staticmethod
    def disconnect(socket):
        """
        disconnects from a given bluetooth device
        :param socket: socket object
        :return: void
        """
        socket.close()
