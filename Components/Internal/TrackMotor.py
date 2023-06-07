import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    ser = serial.Serial()

    def __init__(self, usb):
        self.ser = serial.Serial(port='/dev/tty' + usb, baudrate=115200, timeout=1)  # TODO: change usb to config file

    def activate_motor(self):
        # ControllerData.normalize()
        byte_arr = bytearray([])

        byte_arr.append(int(abs(ControllerData.joystick1[0]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[0] > 0))
        byte_arr.append(int(abs(ControllerData.joystick1[1]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[1] > 0))
        for i in byte_arr:
            print(int(i))
        print(len(byte_arr))

        self.ser.write(byte_arr)
        return  # void

    def __def__(self):
        self.ser.close()
