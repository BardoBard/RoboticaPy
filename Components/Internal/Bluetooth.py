import bluetooth


class Bluetooth:
    buffer_size = 1024

    @staticmethod
    def __find_index(services, name):
        """
        finds index of service, using name
        if name is None it will return the first found index
        :param services: all services
        :param name: name of service
        :return: -1 if name is not found, index if found
        """
        if len(services) == 1 and name is None:
            return 0

        # find the index of connection by name
        for i in range(len(services)):
            if services[i]["name"] == name:
                return i

        print("could not find connection")
        return -1

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
        service_matches = bluetooth.find_service(address=mac_address)

        print("found %d devices" % len(service_matches))

        # if we're unable to find the device return
        index = Bluetooth.__find_index(service_matches, name)

        if index == -1:
            return None

        # connect to mac address using socket
        try:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((mac_address, service_matches[index]["port"]))
            print("connected")
            socket.settimeout(0.5)
            return socket

        except Exception as e:
            if service_matches[index]["name"] is not None:
                print("name: " + service_matches[index]["name"])
            print("port: %d" % service_matches[index]["port"])
            print("protocol: " + service_matches[index]["protocol"])
            print(e)

    @staticmethod
    def check_connection(socket):
        try:
            socket.recv(1)  # TODO: this is a bit slow, maybe check interval instead of pinging
            print("true")
            return True
        except Exception:
            print("error occurred while checking connection")
            return False

    @staticmethod
    def disconnect(socket):
        """
        disconnects from a given bluetooth device
        :param socket: socket object
        :return: void
        """
        socket.close()
