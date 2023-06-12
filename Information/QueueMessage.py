

class QueueMessage:
    def __init__(self, sender, recipient, object):
        self.__sender = sender
        self.__recipient = recipient
        self.__object = object
        
    def get_sender(self):
        return self.__sender
    
    def get_reciepient(self):
        return self.__recipient
    
    def get_object(self):
        return self.__object


    