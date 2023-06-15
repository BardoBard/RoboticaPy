from Wrapper.MessageQueue import MessageQueue
from Information.QueueAgent import QueueAgent
from Information.ImageData import ImageData
from Information.ControllerData import ControllerData
from Components.Internal.Motors.TrackMotor import TrackMotor
from Components.Internal.Motors.ArmMotor import ArmMotor
from Components.Math import Math

import numpy

max_speed = 50

rotation_arm = ArmMotor(2, 1)
left_arm1 = ArmMotor(7, 1)
right_arm1 = ArmMotor(3, 1)
left_arm2 = ArmMotor(10, 1)
right_arm2 = ArmMotor(4, 1)
grabby_arm = ArmMotor(5, 1)


def main_process(queue: MessageQueue):
    latest_image_detection = ImageData(None, None, None, None, None, None, None, None, None, False, None)
    latest_controller_data = None
    mode = manual_control

    # motors = rotation_arm = ArmMotor(2, speed=0),
    # left_arm1 = ArmMotor(7, speed=0),
    # right_arm1 = ArmMotor(3, speed=0),
    # left_arm2 = ArmMotor(10, speed=0),
    # right_arm2 = ArmMotor(4, speed=0),
    # grabber_Arm = ArmMotor(5, speed=0)

    while True:

        # get and process messages to this process
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
    # tracks logic
    joystick1 = controller_data.get_joystick1()
    print("input x: {}, input y: {}".format(joystick1[0], joystick1[1]))

    # rotate
    mapped_values = Math.rotate_tuple_over_origin((joystick1[0], joystick1[1]), 45)
    print("left track: {}, right track: {}".format(mapped_values[0], mapped_values[1]))

    TrackMotor.move(mapped_values[0], mapped_values[1])


def manual_control(controller_data: ControllerData):
    control_tracks(controller_data)
    # joystick2 = controller_data.get_joystick2()
    # rotation_arm.move(300 if numpy.sign(joystick2[0]) < 0 else 1023)
    # rotation_arm.set_speed(numpy.abs(joystick2[0]) * 100)


def manual_arms(controller_data: ControllerData):  # TODO: change it to ArmMotor class, but for now this WORKS
    joystick2 = controller_data.get_joystick2()
    joystick_left_b = controller_data.get_left_b_button()
    joystick_right_b = controller_data.get_right_b_button()

    rotation_speed = int(numpy.abs(joystick2[0]) * max_speed)
    arm_speed = int(numpy.abs(joystick2[1]) * max_speed)
    grabby_speed = (joystick_left_b or joystick_right_b) * max_speed

    rotation_pos = (612 if numpy.sign(joystick2[0]) > 0 else 412)
    left_arm_pos = (712 if numpy.sign(joystick2[1]) > 0 else 312)
    right_arm_pos = (712 if not numpy.sign(joystick2[1]) > 0 else 312)
    grabby_pos = 512

    if joystick_right_b:
        grabby_pos = 312
        grabby_speed = max_speed * 2
    if joystick_left_b:
        grabby_pos = 712
        grabby_speed = max_speed * 2

    print(grabby_speed)

    # print("pos2: " + str(left_arm_pos))
    # print("right_arm_pos: " + str(right_arm_pos))

    if rotation_speed == 0:
        print("rotation_speed 0")
        rotation_speed = 1

    if arm_speed == 0:
        print("rotation_speed 0")
        arm_speed = 1

    if grabby_speed == 0:
        grabby_speed = 1

        # print(rotation_speed)
        # print(arm_speed)
        print("")

    if numpy.abs(joystick2[0]) < 0.2 and numpy.abs(joystick2[1]) < 0.2:
        rotation_arm.set_speed(rotation_speed)
        left_arm1.set_speed(arm_speed)
        right_arm1.set_speed(arm_speed)
        left_arm2.set_speed(arm_speed)
        right_arm2.set_speed(arm_speed)
        grabby_arm.set_speed(grabby_speed)

        rotation_arm.move(rotation_pos)
        left_arm1.move(left_arm_pos)
        right_arm1.move(right_arm_pos)
        left_arm2.move(left_arm_pos)
        right_arm2.move(right_arm_pos)
        grabby_arm.move(grabby_pos)
