import serial as serial

from Information.ControllerData import ControllerData


class TrackMotor:
    serial = None
    serial_port = '/dev/ttyUSB0'  # TODO: change usb to config file

    @staticmethod
    def __getattribute__(name):
        """
        checks connection to the serial port, if there is none it will give an error
        @param name: default __getattribute__ name
        @return: default __getattribute__
        """
        if name == "serial" and TrackMotor.serial is None:
            try:
                TrackMotor.serial = serial.Serial(port=TrackMotor.serial_port, baudrate=115200, timeout=1)
            except Exception:
                print("could not find port")
                TrackMotor.serial = None

        return super().__getattribute__(name)

    @staticmethod
    def move(left_track_speed, right_track_speed):
        """
        moves left and right track motor
        @param left_track_speed: speed of left motor float between [-1-1]
        @param right_track_speed: speed of right motor float between [-1-1]
        @return: void
        """
        if TrackMotor.serial is None:
            return

        byte_arr = bytearray([])

        # left motor
        byte_arr.append(int(abs(left_track_speed) * 255))
        byte_arr.append(bool(left_track_speed > 0))

        # right motor
        byte_arr.append(int(abs(right_track_speed) * 255))
        byte_arr.append(bool(right_track_speed > 0))

        try:
            TrackMotor.serial.write(byte_arr)
        except Exception:
            print("error writing to serial port")

        return  # void
