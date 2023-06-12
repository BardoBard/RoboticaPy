from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix
from multiprocessing import Process
from Information.ImageData import ImageData
from Wrapper.MessageQueue import MessageQueue
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
import time

def detection_process(queue):
    opencv_ = OpenCv()
    
    while True:
        image_data = opencv_.get_image_date_from_feed()
        if image_data.found:
            image_data = scan_data_matrix(image_data)
            queue.send_message(QueueAgent.OPENCV, QueueAgent.CONTROLL, image_data)
                
                
class Controller:
    #controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    #app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    #app_service_name = "APP"
              
    if __name__ == '__main__':
        queue = MessageQueue()
        process = Process(target=detection_process, args=(queue, ))
        process.start() # start the image detection program
        
        time.sleep(15) # capture images for 15 seconds
        
        process.kill() # stop the image detection code
        
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        
        for message in messages:
            message.get_object().print_to_command_line()
        
            
        
        