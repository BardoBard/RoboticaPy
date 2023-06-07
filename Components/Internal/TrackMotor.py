import pigpio
import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)  # TODO: change usb to config file

    @staticmethod
    def activate_motor():
        # ControllerData.normalize()
        byte_arr = bytearray([])

        byte_arr.append(int(abs(ControllerData.joystick1[0]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[0] > 0))
        byte_arr.append(int(abs(ControllerData.joystick1[1]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[1] > 0))
        for i in byte_arr:
            print(int(i))
        print(len(byte_arr))

        TrackMotor.ser.write(byte_arr)
        # time.sleep(10)
        # print(ser.read(5))
        # ser.flush()
        # ser.close()
        return  # void
