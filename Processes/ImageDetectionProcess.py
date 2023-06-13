from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix
from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent

def detection_process(queue: MessageQueue):
    opencv_ = OpenCv()
    while True:
        image_data = opencv_.get_image_date_from_feed()
        if image_data.found:
            image_data = scan_data_matrix(image_data)
            queue.send_message(QueueAgent.OPENCV, QueueAgent.CONTROLL, image_data)