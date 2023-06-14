from multiprocessing import Process

from Components.Internal.Motors.ArmMotor import ArmMotor
from Wrapper.MessageQueue import MessageQueue
from Information.ImageData import ImageData
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
from Information.TelemetryData import TelemetryData

from Processes.BluetoothProcess import bluetooth_client_process
from Processes.ImageDetectionProcess import detection_process

import time

id = 15
speed = 1000
pos = 512
torque = 1023
cw_limit = 0
ccw_limit = 1023

class Controller:
    if __name__ == '__main__':
        # Setup
        print("Hi B^)")

        queue = MessageQueue()
        # image_process = Process(target=detection_process, args=(queue,))
        # bluetooth_process = Process(target=bluetooth_client_process, args=(queue,))
        #
        # image_process.start()  # start the image detection program
        # print("started image detection process at {}".format(image_process.pid))
        #
        # bluetooth_process.start()
        # print("started bluetooth process at {}".format(bluetooth_process.pid))

        # Robot logic
        for i in range(id):
            arm1 = ArmMotor(i, speed)
            arm1.enable_torque(True)
            arm1.set_torque(torque)
            arm1.cw_angle_limit(cw_limit)
            arm1.ccw_angle_limit(ccw_limit)
            arm1.move(pos)
        # arm1.disconnect()

        print("killing proccesses")
        queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH)
        queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.OPENCV)

        print("All done!")
