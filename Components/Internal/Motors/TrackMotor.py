import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    ser = None

    @staticmethod
    def __getattribute__(name):
        if name == "ser" and TrackMotor.ser is None:
            try:
                TrackMotor.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200,
                                               timeout=1)  # TODO: change usb to config file
            except Exception:
                print("could not find port")
                TrackMotor.ser = None

        return super().__getattribute__(name)

    @staticmethod
    def move():
        """
        moves left and right track motor, based on controller values
        @return: void
        """
        if TrackMotor.ser is None:
            return

        # normalize joystick values
        ControllerData.normalize_joysticks()

        byte_arr = bytearray([])

        # left motor
        byte_arr.append(int(abs(ControllerData.joystick1[0]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[0] > 0))

        # right motor
        byte_arr.append(int(abs(ControllerData.joystick1[1]) * 255))
        byte_arr.append(bool(ControllerData.joystick1[1] > 0))

        try:
            TrackMotor.ser.write(byte_arr)
        except Exception:
            print("error writing to serial port")

        return  # void
