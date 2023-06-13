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
from Information.TelemetryData import TelemetryData
import time

def detection_process(queue: MessageQueue):
    opencv_ = OpenCv()
    while True:
        image_data = opencv_.get_image_date_from_feed()
        if image_data.found:
            image_data = scan_data_matrix(image_data)
            queue.send_message(QueueAgent.OPENCV, QueueAgent.CONTROLL, image_data)
            
def bluetooth_client_process(queue: MessageQueue):
    print("starting up bluetooth process")
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    controller_packet_size = 14
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    app_service_name = "APP"
    
    controller_data = ControllerData()
    
    #controller_socket = Socket(controller_mac_address)
    app_socket = Socket(app_mac_address, app_service_name)
    
    print("entering the bluetooth main loop")
    while True:
        print("getting information from the controller")
        #raw_controller_data  = controller_socket.receive(controller_packet_size)
        #controller_data.fill_data(raw_controller_data)
        queue.send_message(QueueAgent.BLUETOOTH, QueueAgent.CONTROLL, controller_data)
        
        messages = queue.get_messages_for(QueueAgent.BLUETOOTH)
        
        if messages is None:
            print("no messages to process on the bluetooth thread")
            continue
        
        #if there are messages we need to process them and act accordingly
        for message in messages:
            data = message.get_object()
            
            #TODO figure out why this doesn't work right with a match statement
            if type(data) is TelemetryData:
                app_socket.send(data.to_json())
            else:
                print("the bluetooth thread was passed an invalid object!")
                

class Controller:
    # @staticmethod
    # def get_controller_data(bluetooth_socket):
    #     arm_motor = ArmMotor(254, 200)  # 254 are all servos
    #     while True:
    #         data = bluetooth_socket.receive(14)
    #         ControllerData.fill_data(data)

    #         ControllerData.normalize_joysticks()

    #         TrackMotor.move(ControllerData.joystick1[0], ControllerData.joystick1[1])
    #         arm_motor.move(0)  # TODO: give arm_motor values
    #         time.sleep(1)
    #         arm_motor.move(500)
    #         time.sleep(1)
    #     # TODO: close all connections + GPIO pins


    if __name__ == '__main__':
        
        # Setup
        print("hi B^)")
        
        queue = MessageQueue()
        image_process = Process(target=detection_process, args=(queue,))
        bluetooth_process = Process(target=bluetooth_client_process, args=(queue, ))
        
        image_process.start()  # start the image detection program
        print("started image detection process at {}".format(image_process.pid))
        
        bluetooth_process.start()
        print("started bluetooth process at {}".format(bluetooth_process.pid))
        
        # Robot logic
        
        #test code
        #send some data to the app
        print("making test data")
        tele_data = TelemetryData()
        print(tele_data.is_modiefied())
        tele_data.set_arm_direction(1)
        print(tele_data.is_modiefied())
        tele_data.set_image_data_code("12323kjdfjk123")
        
        time.sleep(1)
        print("sending test data to bluetooth thread")
        queue.send_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH, tele_data)
        print("done sending test data to bluetooth thread")
        time.sleep(4)
         
        print("getting messages")
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        
        for message in messages:
            print(type(message.get_object()))
        print("done getting messages")
        
        print("killing proccesses")
        image_process.kill()
        bluetooth_process.kill()
        
        print("")
        
        
        
        
