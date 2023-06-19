from Wrapper.Socket import Socket
from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.ControllerData import ControllerData
from Information.TelemetryData import TelemetryData
from Information.QueueKillProcess import QueueKillProcess

def bluetooth_client_process(queue: MessageQueue):
    print("starting up bluetooth process")
    controller_mac_address = "78:21:84:7C:A4:F6"  # controller_mac_address
    controller_packet_size = 14
    app_mac_address = "00:E1:8C:A5:60:44"  # app_mac_address
    app_service_name = "APP"
    
    controller_data = ControllerData()
    
    controller_socket = Socket(controller_mac_address)
    app_socket = Socket(app_mac_address, app_service_name)
    
    run = True
    print("Bluetooth process started")
    while run:
        raw_controller_data  = controller_socket.receive(controller_packet_size)
        if controller_data.fill_data(raw_controller_data):
            queue.send_message(QueueAgent.BLUETOOTH, QueueAgent.CONTROLL, controller_data)
        
        messages = queue.get_messages_for(QueueAgent.BLUETOOTH)
        
        if messages is None:
            continue
        
        #if there are messages we need to process them and act accordingly
        for message in messages:
            data = message.get_object()
            
            #TODO figure out why this doesn't work right with a match statement
            if type(data) is TelemetryData:
                app_socket.send(data.to_json())
            elif type(data) is QueueKillProcess:
                app_socket.close()
                controller_socket.close()
                queue.exit_queue()
                print("shutting down the bluetooth process")
                run = False
                return
            else:
                print("the bluetooth thread was passed an invalid object!")