from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.ImageData import ImageData
from Information.ControllerData import ControllerData
from Components.Internal.Motors.TrackMotor import TrackMotor
from Components.Math import Math



def main_process(queue :MessageQueue):
    latest_image_detection = ImageData(None, None, None, None, None, None , None, None, None, False, None)
    latest_controller_data = ControllerData()
    mode = manual_control
    
    while True:
        
        #get and process messages to this process
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        if messages is not None: 
            for messsage in messages:
                data = messsage.get_object()
                if type(data) is ImageData:
                    latest_image_detection = data
                elif type(data) is ControllerData:
                    latest_controller_data = data
        
        if latest_controller_data.get_left_a_button():
            if mode is not automatic_control:
                print("switching to automatic control")
                mode = automatic_control
        else:
            if mode is not manual_control:
                print("switching to manual control")
                mode = manual_control
          
        
        if shutdown_command(latest_controller_data):
            print("shutting down")
            break
        
        if mode is manual_control:
            manual_control(latest_controller_data)
        elif mode is automatic_control(latest_image_detection):
            automatic_control(latest_image_detection)


        
def shutdown_command(controller_data: ControllerData) -> bool:
    return (controller_data.get_left_b_button() 
            and controller_data.get_right_b_button()
            and controller_data.get_right_a_button())

def automatic_control(image_data: ImageData):
    pass

def manual_control(controller_data: ControllerData):
    #tracks logic
    joystick1 = controller_data.get_joystick1()
    track_input_x = joystick1[0]
    track_input_y = joystick1[1]
    left_motor_val = track_input_x + track_input_y
    right_motor_val = track_input_x - track_input_y
    
    TrackMotor.move(left_motor_val, right_motor_val)
        