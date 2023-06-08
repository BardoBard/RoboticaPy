from Components.Internal.OpenCv import OpenCv
from Components.Internal.DataMatrix import scan_data_matrix
from multiprocessing import Process, Queue

def detection_process(queue):
        opencv_ = OpenCv()
        
        while True:
            print("loop 2")
            image_data = opencv_.get_image_date_from_feed()
            if image_data.found:
                print("detected something!")
                image_data = scan_data_matrix(image_data)
                queue.put(image_data)
                
                
class Controller:
    #controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    #app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    #app_service_name = "APP"
    
    
                
    if __name__ == '__main__':
        queue = Queue()
        process = Process(target=detection_process, args=(queue, ))
        process.start()
        
        while True:
            print("loop1")
            if not queue.empty():
                obj = queue.get()
                print(obj)
            else:
                print(queue.empty())
        