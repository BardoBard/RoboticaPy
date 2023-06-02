import bluetooth

class Bluetooth:
    
    
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
            print(service_matches[i])
            print(service_matches[i]["port"])
            
        
            
            
        
