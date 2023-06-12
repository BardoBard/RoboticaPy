import RPi.GPIO as GPIO
import time

class Eyes:
    def __init__(self, servo1_pin, servo2_pin):
        self.__servo1_pin = servo1_pin
        self.__servo2_pin = servo2_pin
        self.__initialize_gpio()

    def __initialize_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__servo1_pin, GPIO.OUT)
        GPIO.setup(self.__servo2_pin, GPIO.OUT)
        self.__servo1 = GPIO.PWM(self.__servo1_pin, 50)
        self.__servo2 = GPIO.PWM(self.__servo2_pin, 50)
        self.__servo1.start(0)
        self.__servo2.start(0)

    def __set_angle(self, servo, angle):
        duty_cycle = 2 + (angle / 18)
        servo.ChangeDutyCycle(duty_cycle)
        time.sleep(0.3)
        servo.ChangeDutyCycle(0)

    def look_left(self):
        self.__set_angle(self.__servo1, 90)

    def look_right(self):
        self.__set_angle(self.__servo1, 10)

    def look_up(self):
        self.__set_angle(self.__servo2, 10)

    def look_down(self):
        self.__set_angle(self.__servo2, 170)

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
        self.__set_angle(self.__servo1, 90)
        self.__set_angle(self.__servo2, 90)

    def cleanup(self):
        self.__servo1.stop()
        self.__servo2.stop()
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
