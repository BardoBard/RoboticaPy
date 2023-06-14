from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.ImageData import ImageData
from Information.ControllerData import ControllerData
from Components.Internal.Motors.TrackMotor import TrackMotor
from Components.Math import Math



def main_process(queue :MessageQueue):
    latest_image_detection = ImageData(None, None, None, None, None, None , None, None, None, False, None)
    past_controller_data = ControllerData()
    latest_controller_data = ControllerData()
    mode = manual_control
    
    while True:
        
        #get and process messages to this process
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        if messages is not None: 
            for message in messages:
                data = message.get_object()
                if type(data) is ImageData:
                    latest_image_detection = data
                elif type(data) is ControllerData:
                    past_controller_data = latest_controller_data
                    latest_controller_data = data
                    mode = switch_mode(mode)
                    on_controller_data(latest_controller_data, past_controller_data, mode, latest_image_detection)
                    
                        
def on_controller_data(controller_data: ControllerData, past_controller_data: ControllerData, mode, image_data):
    if mode is automatic_control:
        automatic_control(image_data)
    elif mode is manual_control:
        manual_control(controller_data, past_controller_data)


def switch_mode(mode, button):
    if button:
        if mode is not manual_control:
            print("switching to manual control")
            mode_ = manual_control
    else:
        if mode is not automatic_control:
            print("switching to automatic control")
            mode_ = automatic_control
    return mode_

def shutdown_command(controller_data: ControllerData) -> bool:
    return (controller_data.get_left_b_button() 
            and controller_data.get_right_b_button()
            and controller_data.get_right_a_button())

def automatic_control(image_data: ImageData):
    pass

def manual_control(controller_data: ControllerData, past_controller_data: ControllerData):
    #tracks logic
    if controller_data.__eq__(past_controller_data):
        print("returning because there's no new data")
        return
    
    joystick1 = controller_data.get_joystick1()
    print("input x: {}, input y: {}".format(joystick1[0], joystick1[1]))
    
    #mirror the axis
    joystick1 = (-joystick1[0], joystick1[1])
    
    #rotate
    mapped_values = Math.rotate_tuple_over_origin(joystick1, 45)
    print("left track: {}, right track: {}".format(mapped_values[0], mapped_values[1]))
    
    TrackMotor.move(mapped_values[0], mapped_values[1])
        