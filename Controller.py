from multiprocessing import Process

import numpy

from Components.Internal.Motors.ArmMotor import ArmMotor
from Information.ControllerData import ControllerData
from Wrapper.MessageQueue import MessageQueue
from Information.ImageData import ImageData
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
from Information.TelemetryData import TelemetryData

from Processes.BluetoothProcess import bluetooth_client_process
from Processes.ImageDetectionProcess import detection_process
from Processes.MainProcess import main_process

import traceback
import time

from Wrapper.Socket import Socket

speed = 50
original_pos = 512
pos = 100
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

        rotation_arm = ArmMotor(2, speed=100)
        controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
        controller_packet_size = 14
        # app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
        # app_service_name = "APP"

        controller_data = ControllerData()

        controller_socket = Socket(controller_mac_address)

        rotation_servo = ArmMotor(2, speed)
        left_arm1 = ArmMotor(7, speed)
        right_arm1 = ArmMotor(3, speed)
        left_arm2 = ArmMotor(10, speed)
        right_arm2 = ArmMotor(4, speed)

        while True:
            pos2 = -pos if controller_data.get_joystick2()[0] > 0 else pos
            pos3 = -pos if controller_data.get_joystick2()[1] > 0 else pos
            rotation_servo.move(original_pos + pos2)
            left_arm1.move(original_pos + pos3)
            right_arm1.move(original_pos - pos3)
            left_arm2.move(original_pos - pos3)
            right_arm2.move(original_pos + pos3)

        print("killing proccesses")
        # queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH)
        # queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.OPENCV)
        #
        # bluetooth_process.join()
        # image_process.join()
        print("All done!")
