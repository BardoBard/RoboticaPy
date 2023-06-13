import struct

from Components.Math import Math


class ControllerData:
    """
    data class for controller
    """

    def __init__(self, data=None):        
        self.__joystick1 = (0, 0)
        self.__joystick1_click = False
        self.__joystick2 = (0, 0)
        self.__joystick2_click = False
        self.__LA = False
        self.__LB = False
        self.__RA = False
        self.__RB = False
        
        if data is not None:
            self.fill_data(data)

    
    def fill_data(self, data):
        """
        fills and normalizes the controller data
        :param data: 14 byte array
        :return: void
        """
        if data and len(data) == 14:
            # joystick left (x,y)
            self.__joystick1 = struct.unpack('H' * 2, data[0:4])
            self.__joystick1_click = bool(data[4])

            # joystick right (x,y)
            self.__joystick2 = struct.unpack("H" * 2, data[5:9])
            self.__joystick2_click = bool(data[9])

            # buttons on controller
            self.__LA = bool(data[10])
            self.__LB = bool(data[11])
            self.__RA = bool(data[12])
            self.__RB = bool(data[13])
            
            self.__normalize_joysticks()

    def __normalize_joysticks(self):
        # TODO: make magic numbers generic
        # TODO: probably should return normalized data instead of changing current data

        # joystick 1
        self.__joystick1 = (Math.normalize_neg(self.__joystick1[0], 725, 2900),
                                    -Math.normalize_neg(self.__joystick1[1], 0, 2760))

        # joystick 2
        self.__joystick2 = (Math.normalize_neg(self.__joystick2[0], 800, 3100),
                                    -Math.normalize_neg(self.__joystick2[1], 630, 3000))
