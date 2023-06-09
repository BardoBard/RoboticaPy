import time

import pigpio
import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    ser = None

    # def __init__(self):
    def __getattribute__(self, name):
        if name == "ser":
            try:
                time.sleep(0.5)
                self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200,
                                         timeout=1)  # TODO: change usb to config file
            finally:
                print("could not find port")
        return object.__getattribute__(self)

    @staticmethod
    def activate_motor():
        if TrackMotor.ser is None:
            return
        # ControllerData.normalize()
        byte_arr = bytearray([])

        byte_arr.append(int(abs(ControllerData.joystick1[0]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[0] > 0))
        byte_arr.append(int(abs(ControllerData.joystick1[1]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[1] > 0))

        TrackMotor.ser.write(byte_arr)
        return  # void
