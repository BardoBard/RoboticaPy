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
                data = socket.recy(self.buffer_size)
                if data:
                    print(data)
            
            
            
        
