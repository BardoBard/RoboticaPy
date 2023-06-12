from Components.Internal.Motors.ArmMotor import ArmMotor
from Components.Internal.Motors.TrackMotor import TrackMotor
from Information.ControllerData import ControllerData
from Wrapper.Socket import Socket


class Controller:
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address

    @staticmethod
    def get_controller_data(bluetooth_socket):
        ArmMotor.initialize()
        arm_motor = ArmMotor(254, 10)  # 254 are all servos
        while True:
            data = bluetooth_socket.receive(14)
            ControllerData.fill_data(data)
            TrackMotor.move()
            arm_motor.move(5)  # TODO: give arm_motor values
        # TODO: close all connections + GPIO pins

    def remote_to_arm(self, value):
        return  # void

    def weight_to_text(self, weight):  # not sure what this does, perhaps not necessary
        return  # void

    def turn_led_on(self, frequency):
        return  # void

    def detect_object(self):
        return  # void
