from gpiozero import DistanceSensor as DS #library built on top of rpi.gpio and pigpio


class DistanceSensor:

    sensor = DS(23,24) #random pins need to be changed later

    def find_distance(self):
        a = DS.sensor.distance
        return
