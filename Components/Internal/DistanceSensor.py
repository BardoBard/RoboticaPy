import pigpio

class DistanceSensor:
    pi1 = pigpio.pi()

    pin_trigger = 23
    pin_echo = 24

    def find_distance(self):

        self.pi1.set_mode(self.pin_trigger, pigpio.OUTPUT)
        self.pi1.write(self.pin_trigger, 0)
        self.pi1.set_mode(self.pin_echo, pigpio.INPUT)
        #add more stuff to read distance.
        return
