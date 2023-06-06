import pigpio
import serial as serial


class TrackMotor:
    @staticmethod
    def activate_motor():
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
        ser.write("hi")
        ser.close()
        return  # void
