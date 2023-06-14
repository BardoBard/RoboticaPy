import numpy
from pyax12.connection import Connection

from Components.Internal.Motors.ArmMotor import ArmMotor
from Information.ControllerData import ControllerData

import time

from Wrapper.Socket import Socket

speed = 50
original_pos = 512
pos = original_pos
pos2 = original_pos
torque = 1023
cw_limit = 0
ccw_limit = 1023


class Controller:
    if __name__ == '__main__':
        # Setup
        print("Hi B^)")

        # queue = MessageQueue()
        # image_process = Process(target=detection_process, args=(queue,))
        # bluetooth_process = Process(target=bluetooth_client_process, args=(queue, ))

        # image_process.start()  # start the image detection program
        # print("started image detection process at {}".format(image_process.pid))

        # bluetooth_process.start()
        # print("started bluetooth process at {}".format(bluetooth_process.pid))

        # Robot logic
        # try:
        #     main_process(queue)
        # except Exception as e:
        #     print("FATAL ERROR!")
        #     print(traceback.format_exc())

        # rotation_arm = ArmMotor(2, speed=100)
        controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
        controller_packet_size = 14
        # app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
        # app_service_name = "APP"

        controller_data = ControllerData()

        controller_socket = Socket(controller_mac_address)

        serial_connection = Connection(port="/dev/ttyS0", baudrate=1_000_000, timeout=0.05)

        serial_connection.pretty_print_control_table(2)

        serial_connection.close()

        print("killing proccesses")
        # queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH)
        # queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.OPENCV)
        #
        # bluetooth_process.join()
        # image_process.join()
        print("All done!")
