import pigpio
import serial as serial


class TrackMotor:
    @staticmethod
    def activate_motor():
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)  # TODO: change usb to config file
        packet = bytearray()
        packet.append(0xFF)
        packet.append(0xFF)
        ser.write(packet)
        ser.close()
        return  # void
