import pigpio
import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    @staticmethod
    def activate_motor():
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)  # TODO: change usb to config file
        # ControllerData.normalize()
        byte_arr = bytearray([0, 0, 0, 0])

        byte_arr[0] = (int(abs(ControllerData.joystick1[0]) * 255)).to_bytes(1, 'little')
        byte_arr[1] = bool(ControllerData.joystick1[0] > 0)
        byte_arr[2] = (int(abs(ControllerData.joystick1[1]) * 255)).to_bytes(1, 'little')
        byte_arr[3] = bool(ControllerData.joystick1[1] > 0)
        print(len(byte_arr))

        ser.write(byte_arr)
        # ser.close()
        return  # void
