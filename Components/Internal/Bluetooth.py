import struct
import bluetooth

class Bluetooth:
    buffer_size = 1024
    
    def scan(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True) 
        print("found %d devices" % len(nearby_devices)) 
        
        for addr, name in nearby_devices: 
            print(" %s - %s" % (addr, name))
            
    def connect(self, mac_addresss):
        service_matches = bluetooth.find_service(address = mac_addresss)
        print("found %d services" % len(service_matches))
        
        if(len(service_matches) == 0):
            print("no services found")
            return
        
        for i in range(len(service_matches)):
            print("name: " + service_matches[i]["name"])
            print("port: %d" % service_matches[i]["port"])
            print("protocol: " + service_matches[i]["protocol"])
        
        if(len(service_matches) == 1):
            print("connecting")
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((mac_addresss, service_matches[0]["port"]))          
            print("connected")
            socket.send("hi")
            
            while True:
                data = socket.recv(self.buffer_size)
                if data:
                    byte_arr = bytes(data)
                    joystick1 = struct.unpack('H' * 2, byte_arr[0:4])
                    joystick1_click = bool(byte_arr[4])
                    joystick2 = struct.unpack("H" * 2, byte_arr[5:9])
                    joystick2_click = bool(byte_arr[9])
                    LA = bool(byte_arr[10])
                    LB = bool(byte_arr[11])
                    RA = bool(byte_arr[12])
                    RB = bool(byte_arr[13])

                    print("joystick x: ", joystick1[0])
                    print("joystick y: ", joystick1[1])
                    print("joystick1 bool: ", joystick1_click)
                    print("joystick2 x: ", joystick2[0])
                    print("joystick2 y: ", joystick2[1])
                    print("joystick2 click: ", joystick2_click)
                    print("LA: ", LA)
                    print("LB: ", LB)
                    print("RA: ", RA)
                    print("RB: ", RB)

            
            
            
        
