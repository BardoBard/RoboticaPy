import RPi.GPIO as GPIO
import time

class Eyes:
    def __init__(self, servo1_pin, servo2_pin):
        self.servo1_pin = servo1_pin
        self.servo2_pin = servo2_pin
        self.initialize_gpio()

    def initialize_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo1_pin, GPIO.OUT)
        GPIO.setup(self.servo2_pin, GPIO.OUT)
        self.servo1 = GPIO.PWM(self.servo1_pin, 50)
        self.servo2 = GPIO.PWM(self.servo2_pin, 50)
        self.servo1.start(0)
        self.servo2.start(0)

    def set_angle(self, servo, angle):
        duty_cycle = 2 + (angle / 18)
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.3)
        servo.ChangeDutyCycle(0)

    def look_left(self):
        self.set_angle(self.servo1, 90)

    def look_right(self):
        self.set_angle(self.servo1, 10)

    def look_up(self):
        self.set_angle(self.servo2, 10)

    def look_down(self):
        self.set_angle(self.servo2, 170)

    def happy(self):
        self.look_up()
        self.look_left()

    def sad(self):
        self.look_down()
        self.look_right()

    def surprised(self):
        self.look_up()
        self.look_right()

    def angry(self):
        self.look_down()
        self.look_left()

    def neutral(self):
        self.set_angle(self.servo1, 90)
        self.set_angle(self.servo2, 90)

    def cleanup(self):
        self.servo1.stop()
        self.servo2.stop()
        GPIO.cleanup()

# Usage example
if __name__ == '__main__':
    # Pin numbers for the servos
    servo1_pin = 11
    servo2_pin = 13

    # Create an instance of the Eyes class
    walle = Eyes(servo1_pin, servo2_pin)

    # Perform different emotions
    walle.happy()
    time.sleep(1)
    walle.sad()
    time.sleep(1)
    walle.surprised()
    time.sleep(1)
    walle.angry()
    time.sleep(1)
    walle.neutral()

    # Clean up GPIO resources
    walle.cleanup()
