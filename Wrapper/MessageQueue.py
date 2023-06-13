from multiprocessing import Process, Queue
from Information.QueueMessage import QueueMessage
from Information.QueueAgent import QueueAgent
from typing import List

class MessageQueue:
    def __init__(self):
        self.__queue = Queue()
        
    def exit_queue(self):
        """You need to call this from any process that uses the queue before you kill that process.
        """
        self.__queue.close()
    
    def get_messages_for(self, queue_agent) -> List[QueueMessage]:
        """gets all the messages for a queue agent

        Args:
            queue_agent (QueueAgent): the process that you call this from

        Returns:
            a list of messages or None: the messages for this recipient
        """ 
        if self.__queue.empty():
            return None
        
        all_messages = []
        #Get all the messages from the queue
        while self.__queue.qsize() > 0:
            # WARNING: This will hang if one of the processes is killed without calling exit_queue from it
            all_messages.append(self.__queue.get())
        
        return_messages = []
        unreturned_messages = []
        
        # Filter through all the messages that are currently in the queue
        for message in all_messages:
            if message.get_recipient() is queue_agent:
                return_messages.append(message)
            else:
                unreturned_messages.append(message)
        
        # Put the messages that weren't meant for us back in the queue
        for message in unreturned_messages:
            self.__queue.put(message)
                
        return return_messages
        
    
    def send_message(self, sender, recipient, obj):
        """Sends a message over the queue

        Args:
            sender (QueueAgent): the process that's sending the message
            recipient (QueueAgent): the process that's intended to recieve the message
            obj (object): any object
        """
        self.__queue.put(QueueMessage(sender, recipient, obj))