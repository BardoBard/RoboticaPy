import struct

import numpy

from Components.Math import Math


class ControllerData:
    """
    data class for controller
    """
    joystick1 = (0, 0)
    joystick1_click = False
    joystick2 = (0, 0)
    joystick2_click = False
    LA = False
    LB = False
    RA = False
    RB = False

    @staticmethod
    def fill_data(data):
        """
        fills the controller data
        :param data: 14 bytes array
        :return: void
        """
        if data:
            byte_arr = bytes(data)
            ControllerData.joystick1 = struct.unpack('H' * 2, byte_arr[0:4])
            ControllerData.joystick1_click = bool(byte_arr[4])
            ControllerData.joystick2 = struct.unpack("H" * 2, byte_arr[5:9])
            ControllerData.joystick2_click = bool(byte_arr[9])
            ControllerData.LA = bool(byte_arr[10])
            ControllerData.LB = bool(byte_arr[11])
            ControllerData.RA = bool(byte_arr[12])
            ControllerData.RB = bool(byte_arr[13])

            print("joystick x: ", ControllerData.joystick1[0])
            print("joystick y: ", ControllerData.joystick1[1])
            print("joystick1 bool: ", ControllerData.joystick1_click)
            print("joystick2 x: ", ControllerData.joystick2[0])
            print("joystick2 y: ", ControllerData.joystick2[1])
            print("joystick2 click: ", ControllerData.joystick2_click)
            print("LA: ", ControllerData.LA)
            print("LB: ", ControllerData.LB)
            print("RA: ", ControllerData.RA)
            print("RB: ", ControllerData.RB)
            ControllerData.normalize()
            print("\\n")

    @staticmethod
    def normalize():
        ControllerData.joystick1 = (Math.normalize_neg_one(ControllerData.joystick1[0], 725, 2900),
                                    Math.normalize_neg_one(ControllerData.joystick1[1], 0, 2750))
        print("joystick1 x: ", ControllerData.joystick1[0])
        print("joystick1 y: ", ControllerData.joystick1[1])
