from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix
from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.QueueKillProcess import QueueKillProcess

def detection_process(queue: MessageQueue):
    print("starting up the opencv process")
    opencv_ = OpenCv()
    while True:
        image_data = opencv_.get_image_date_from_feed()
        if image_data.found:
            image_data = scan_data_matrix(image_data)
            queue.send_message(QueueAgent.OPENCV, QueueAgent.CONTROLL, image_data)
            
        messages = queue.get_messages_for(QueueAgent.OPENCV)
        if messages is None:
            continue
        
        for message in messages:
            data = message.get_object()
            
            if type(data) is QueueKillProcess:
                #TODO shutdown code
                queue.exit_queue()
                print("shutting down the opencv process")
                break