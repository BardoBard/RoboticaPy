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
        self.__prev_RA = False

        if data is not None:
            self.fill_data(data)

    def __eq__(self, __value: object) -> bool:
        if type(__value) is ControllerData:
            print("comparing values")
            return (__value.get_joystick1() is self.__joystick1 and
                    __value.get_joystick1_click() is self.__joystick1_click and
                    __value.get_joystick2() is self.__joystick2 and
                    __value.get_joystick2_click() is self.__joystick2_click and
                    __value.get_left_a_button() is self.__LA and
                    __value.get_left_b_button() is self.__LB and
                    __value.get_right_a_button() is self.__RA and
                    __value.get_right_b_button() is self.__RB)
        else:
            print("different types")
            return False
            
        
        
    #getters
    def get_joystick1(self) -> tuple[float, float]:
        return self.__joystick1
    
    def get_joystick1_click(self) -> bool:
        return self.__joystick1_click
    
    def get_joystick2 (self) -> tuple[float, float]:
        return self.__joystick2
    
    def get_joystick2_click(self) -> bool:
        return self.__joystick2_click

    def get_left_a_button(self) -> bool:
        return self.__LA
    
    def get_left_b_button(self) -> bool:
        return self.__LB
    
    def get_right_a_button(self) -> bool:
        return self.__RA
    
    def get_right_b_button(self) -> bool:
        return self.__RB
    
    def fill_data(self, data):
        """
        fills and normalizes the controller data
        :param data: 14 byte array
        :return: void
        """
        if not data or len(data) != 14:
            return False
        
        # joystick left (x,y)
        self.__joystick1 = struct.unpack('H' * 2, data[0:4])
        self.__joystick1_click = bool(data[4])

        # joystick right (x,y)
        self.__joystick2 = struct.unpack("H" * 2, data[5:9])
        self.__joystick2_click = bool(data[9])

        # buttons on controller
        self.__LA = bool(data[10])
        self.__LB = bool(data[11])
        self.__RB = bool(data[12])

        self.__RA = bool(data[13])
        if self.__RA and not self.__prev_RA: #TODO: remove this
            self.__prev_RA = self.__RA
            self.__RA = not self.__RA
        else:
            self.__prev_RA = self.__RA
        
        self.__normalize_joysticks()
        
        return True

    def __normalize_joysticks(self):
        # TODO: make magic numbers generic
        # TODO: probably should return normalized data instead of changing current data

        # joystick 1
        self.__joystick1 = (Math.normalize_neg(self.__joystick1[0], 725, 2900),
                                    -Math.normalize_neg(self.__joystick1[1], 0, 2760))

        # joystick 2
        self.__joystick2 = (Math.normalize_neg(self.__joystick2[0], 800, 3100),
                                    -Math.normalize_neg(self.__joystick2[1], 630, 3000))
