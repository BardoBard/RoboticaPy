import serial as serial


class TrackMotor:
    serial = None
    serial_port = '/dev/ttyUSB0'  # TODO: change usb to config file

    @classmethod
    def get_serial(cls):
        """
        checks connection to the serial port, if there is none it will give an error
        @return: serial or None
        """
        print("check")
        if cls.serial is None:
            try:
                cls.serial = serial.Serial(port=cls.serial_port, baudrate=115200, timeout=1)
            except Exception:
                print("could not find port")
                cls.serial = None

        return cls.serial

    @staticmethod
    def move(left_track_speed, right_track_speed):
        """
        moves left and right track motor
        @param left_track_speed: speed of left motor float between [-1-1]
        @param right_track_speed: speed of right motor float between [-1-1]
        @return: void
        """
        if TrackMotor.get_serial is None:
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
