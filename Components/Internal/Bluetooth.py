from bluetooth import *

class Bluetooth:
    
    
    def scan(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True) 
        print("found %d devices" % len(nearby_devices)) 
        
        for addr, name in nearby_devices: 
            print(" %s - %s" % (addr, name))
            
    def connect(self, mac_addresss):
        service_matches = find_service(mac_addresss)
        print("found %d services" % len(service_matches))
        for i in range(len(service_matches)):
            print(service_matches[i])
