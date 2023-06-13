from multiprocessing import Process
from Wrapper.MessageQueue import MessageQueue
from Information.ImageData import ImageData
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
from Information.TelemetryData import TelemetryData

from Processes.BluetoothProcess import bluetooth_client_process
from Processes.ImageDetectionProcess import detection_process

import time
                
class Controller:
    if __name__ == '__main__':
        
        # Setup
        print("Hi B^)")
        
        queue = MessageQueue()
        #image_process = Process(target=detection_process, args=(queue,))
        bluetooth_process = Process(target=bluetooth_client_process, args=(queue, ))
        
        #image_process.start()  # start the image detection program
        print("started image detection process at {}".format(image_process.pid))
        
        bluetooth_process.start()
        print("started bluetooth process at {}".format(bluetooth_process.pid))
        
        # Robot logic
        tele = TelemetryData()
        tele.set_arm_direction(1)
        tele.set_direction(2)
        tele.set_image_data_code(3)
        
        queue.send_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH, tele)
        
        print("killing proccesses")
        queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH)
        #queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.OPENCV)
        
        print("All done!")