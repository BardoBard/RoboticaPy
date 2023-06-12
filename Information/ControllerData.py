import struct

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
        :param data: 14 byte array
        :return: void
        """
        if data and len(data) == 14:
            # joystick left (x,y)
            ControllerData.joystick1 = struct.unpack('H' * 2, data[0:4])
            ControllerData.joystick1_click = bool(data[4])

            # joystick right (x,y)
            ControllerData.joystick2 = struct.unpack("H" * 2, data[5:9])
            ControllerData.joystick2_click = bool(data[9])

            # buttons on controller
            ControllerData.LA = bool(data[10])
            ControllerData.LB = bool(data[11])
            ControllerData.RA = bool(data[12])
            ControllerData.RB = bool(data[13])

            # print("joystick x: ", ControllerData.joystick1[0])
            # print("joystick y: ", ControllerData.joystick1[1])
            # print("joystick1 bool: ", ControllerData.joystick1_click)
            # print("joystick2 x: ", ControllerData.joystick2[0])
            # print("joystick2 y: ", ControllerData.joystick2[1])
            # print("joystick2 click: ", ControllerData.joystick2_click)
            # print("LA: ", ControllerData.LA)
            # print("LB: ", ControllerData.LB)
            # print("RA: ", ControllerData.RA)
            # print("RB: ", ControllerData.RB)

    @staticmethod
    def normalize_joysticks():
        # TODO: make magic numbers generic
        # TODO: probably should return normalized data instead of changing current data
        ControllerData.joystick1 = (Math.normalize_neg(ControllerData.joystick1[0], 725, 2900),
                                    -Math.normalize_neg(ControllerData.joystick1[1], 0, 2760))
        ControllerData.joystick2 = (Math.normalize_neg(ControllerData.joystick2[0], 800, 3100),
                                    -Math.normalize_neg(ControllerData.joystick2[1], 630, 3000))
        print("joystick1 x: ", ControllerData.joystick1[0])
        print("joystick1 y: ", ControllerData.joystick1[1])
        print("joystick2 x: ", ControllerData.joystick2[0])
        print("joystick2 y: ", ControllerData.joystick2[1])
