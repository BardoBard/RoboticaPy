import pigpio
import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    @staticmethod
    def activate_motor():
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)  # TODO: change usb to config file
        # ControllerData.normalize()
        byte_arr = bytearray(
            [1, 2, 3, 4])

        print(len(byte_arr))

        ser.write(byte_arr)
        # ser.close()
        return  # void
