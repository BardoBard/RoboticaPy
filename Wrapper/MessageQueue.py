from multiprocessing import Process, Queue
from Information.QueueMessage import QueueMessage

class MessageQueue:
    def __init__(self):
        self.__queue = Queue()
        print("queue instantiated")
        
    def get_queue(self):
        return self.__queue
    
    def get_messages_for(self, queue_agent):
        print("getting messages")
        if self.__queue.empty():
            print("queue was empty")
            return None
        
        all_messages = []
        #get all the messages from the queue
        while self.__queue.qsize() > 0:
            print("queue size is: {}".format( self.__queue.qsize()))
            all_messages.append(self.__queue.get_nowait())
            print("queue size is: {}".format( self.__queue.qsize()))
        
        return_messages = []
        unreturned_messages = []
        
        for message in all_messages:
            if message.get_recipient() is queue_agent:
                return_messages.append(message)
            else:
                unreturned_messages.append(message)
        
        for message in unreturned_messages:
            self.__queue.put(message)
            
        return return_messages
        
    def send_message(self, sender, recipient, obj):
        print("sending message from {} to {} ".format(sender, recipient))
        self.__queue.put(QueueMessage(sender, recipient, obj))