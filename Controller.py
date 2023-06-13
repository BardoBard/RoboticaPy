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
        print(tele_data.is_modified())
        tele_data.set_arm_direction(1)
        print(tele_data.is_modified())
        tele_data.set_image_data_code("12323kjdfjk123")
        
        time.sleep(1)
        print("sending test data to bluetooth thread")
        queue.send_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH, tele_data)
        print("done sending test data to bluetooth thread")
        time.sleep(1)
         
        print("getting messages")
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        if messages is not None:
            for message in messages:
                print(type(message.get_object()))
        print("done getting messages")
        
        print("killing proccesses")
        queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.BLUETOOTH)
        queue.send_kill_message(QueueAgent.CONTROLL, QueueAgent.OPENCV)
        
        print("All done!")