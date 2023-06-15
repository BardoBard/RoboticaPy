import serial
import time
import RPi.GPIO as GPIO
import sys

class AX12:
    def __init__(self, port="/dev/ttyS0", baudrate=1000000):
        self.rpi_gpio = True

        if self.rpi_gpio:
            if "RPi" in sys.modules:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(18, GPIO.OUT)
            else:
                raise Exception("RPi.GPIO cannot be imported")

        self.serial_connection = serial.Serial(port=port, baudrate=baudrate, timeout=0.1,
                                               bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                               stopbits=serial.STOPBITS_ONE)

    def send(self, instruction_packet):
        if isinstance(instruction_packet, bytes):
            instruction_packet_bytes = instruction_packet
        else:
            instruction_packet_bytes = instruction_packet.to_bytes()

        self.flush()

        if self.rpi_gpio:
            GPIO.output(18, GPIO.HIGH)
            time.sleep(0.01)

        self.serial_connection.write(instruction_packet_bytes)

        if self.rpi_gpio:
            self.serial_connection.flushOutput()
            time.sleep(0.00017 * len(instruction_packet_bytes))
            GPIO.output(18, GPIO.LOW)
            time.sleep(0.004)
        else:
            time.sleep(0.02)

    def flush(self):
        if self.rpi_gpio:
            self.serial_connection.flushInput()
            self.serial_connection.flushOutput()
        else:
            time.sleep(0.01)  # Adjust delay as needed

    def close(self):
        self.serial_connection.close()
        if self.rpi_gpio:
            GPIO.cleanup()

    def goto(self, servo_id, position, speed=None, degrees=True):
        if degrees:
            position = self._convert_degrees_to_position(position)

        data = [position & 0xFF, (position >> 8) & 0xFF]

        if speed is not None:
            data.extend([speed & 0xFF, (speed >> 8) & 0xFF])

        instruction_packet = self._create_instruction_packet(servo_id, 5, data)
        self.send(instruction_packet)

    def _convert_degrees_to_position(self, degrees):
        return int((degrees / 300) * 1023)

    def _create_instruction_packet(self, servo_id, action, data):
        instruction_packet = bytearray([0xFF, 0xFF, servo_id, action, len(data) + 2]) + bytearray(data)
        checksum = sum(instruction_packet) & 0xFF
        instruction_packet.append(0xFF - checksum)
        return instruction_packet

if __name__ == "main":
    ax12 = AX12()

    try:
        ax12.goto(2, 512, 50, degrees=False)
        # now move it back
        ax12.goto(2, 400, 50, degrees=False)
    except:
        print("error while closing down")

    ax12.close()