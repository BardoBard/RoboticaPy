from multiprocessing import Process, Queue
from Information.QueueMessage import QueueMessage

class MessageQueue:
    def __init__(self):
        self.__queue = Queue()
        
    def exit_queue(self):
        self.__queue.close()
        
    def get_queue(self):
        return self.__queue
    
    def get_messages_for(self, queue_agent):
        if self.__queue.empty():
            return None
        
        all_messages = []
        #Get all the messages from the queue
        while self.__queue.qsize() > 0:
            # WARNING: This will hang if one of the processes is killed without calling exit queue from it
            # It 
            all_messages.append(self.__queue.get())
        
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
        self.__queue.put(QueueMessage(sender, recipient, obj))