from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.ImageData import ImageData
from Information.ControllerData import ControllerData
from Components.Internal.Motors.TrackMotor import TrackMotor
from Components.Internal.Motors.ArmMotor import ArmMotor
from Components.Math import Math

import numpy

rotation_arm = ArmMotor(2, speed=10)
left_arm1 = ArmMotor(7, speed=0)
right_arm1 = ArmMotor(3, speed=0)
left_arm2 = ArmMotor(10, speed=0)
right_arm2 = ArmMotor(4, speed=0)
grabber_Arm = ArmMotor(5, speed=0)


def main_process(queue :MessageQueue):
    latest_image_detection = ImageData(None, None, None, None, None, None , None, None, None, False, None)
    latest_controller_data = None
    mode = manual_control


    while True:

        #get and process messages to this process
        messages = queue.get_messages_for(QueueAgent.CONTROLL)
        if messages is None:
            continue

        for message in messages:
            print("processing message")
            data = message.get_object()
            if type(data) is ImageData:
                latest_image_detection = data
                if mode is automatic_control:
                    automatic_control(latest_image_detection)
            elif type(data) is ControllerData:
                latest_controller_data = data
                mode = switch_mode(mode, latest_controller_data.get_left_a_button())
                if shutdown_command(latest_controller_data):
                    print("shutting down main thread")
                    TrackMotor.move(0, 0)
                    return
                if mode is manual_control:
                    manual_control(latest_controller_data)


def switch_mode(mode, button):
    if button:
        if mode is not manual_control:
            print("switching to manual control")
            return manual_control
    else:
        if mode is not automatic_control:
            print("switching to automatic control")
            return automatic_control

def shutdown_command(controller_data: ControllerData) -> bool:
    return (controller_data.get_left_b_button()
            and controller_data.get_right_b_button()
            and controller_data.get_right_a_button())

def automatic_control(image_data: ImageData):
    print("movex{}".format(image_data.movex))

def control_tracks(controller_data: ControllerData):
    #tracks logic
    joystick1 = controller_data.get_joystick1()
    # print("input x: {}, input y: {}".format(joystick1[0], joystick1[1]))

    #rotate
    mapped_values = Math.rotate_tuple_over_origin((joystick1[0], joystick1[1]), 45)
    # print("left track: {}, right track: {}".format(mapped_values[0], mapped_values[1]))

    # TrackMotor.move(mapped_values[0], mapped_values[1])

def move_arm(controller_data: ControllerData):
    joystick2 = controller_data.get_joystick2()
    print(400 if numpy.sign(joystick2[0]) < 0 else 600)
    print(int(numpy.abs(joystick2[0]) * 150))
    print("")
    # rotation_arm.set_speed(int(numpy.abs(joystick2[0]) * 150))
    rotation_arm.move(400 if numpy.sign(joystick2[0]) < 0 else 600)


def manual_control(controller_data: ControllerData):
    control_tracks(controller_data)
    move_arm(controller_data)
