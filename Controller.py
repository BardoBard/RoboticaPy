from Components.Internal.Motors.ArmMotor import ArmMotor
from Components.Internal.Motors.TrackMotor import TrackMotor
from Information.ControllerData import ControllerData
from Wrapper.Socket import Socket
from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix
from multiprocessing import Process
from Information.ImageData import ImageData
from Wrapper.MessageQueue import MessageQueue
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
import time


class Controller:
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address

    @staticmethod
    def get_controller_data(bluetooth_socket):
        arm_motor = ArmMotor(254, 10)  # 254 are all servos
        while True:
            data = bluetooth_socket.receive(14)
            ControllerData.fill_data(data)

            ControllerData.normalize_joysticks()

            print("moving")
            TrackMotor.move(ControllerData.joystick1[0], ControllerData.joystick1[1])
            print("moving2")
            arm_motor.move(10)  # TODO: give arm_motor values
            time.sleep(1)
            arm_motor.move(500)
            time.sleep(1)
        # TODO: close all connections + GPIO pins

    socket = Socket(controller_mac_address)
    get_controller_data(socket)
    # controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    # app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    # app_service_name = "APP"
    def detection_process(queue):

        opencv_ = OpenCv()

    while True:
        image_data = opencv_.get_image_date_from_feed()
        if image_data.found:
            image_data = scan_data_matrix(image_data)
            queue.send_message(QueueAgent.OPENCV, QueueAgent.CONTROLL, image_data)

    if __name__ == '__main__':
        print("hi B^)")
        queue = MessageQueue()
        process = Process(target=detection_process, args=(queue,))
        process.start()  # start the image detection program
        print("started process at {}".format(process.pid))
        time.sleep(5)  # capture images for 5 seconds
        print("done sleeping")
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        print("got messages from the queue")
        for message in messages:
            message.get_object().print_to_command_line()

        process.kill()  # stop the image detection code
        print("killed process")
