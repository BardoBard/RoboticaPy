import serial
import time
import RPi.GPIO as GPIO

class AX12:
    def __init__(self, port="/dev/ttyS0", baudrate=1000000):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        
        self.port = serial.Serial(port, baudrate=baudrate, timeout=3.0)
    
    def goto(self, servo_id, position, speed=None, degrees=True):
        if degrees:
            position = self._convert_degrees_to_position(position)
        
        data = [position & 0xFF, (position >> 8) & 0xFF]
        
        if speed is not None:
            data.extend([speed & 0xFF, (speed >> 8) & 0xFF])
        
        self._send_command(servo_id, 5, data)
    
    def _convert_degrees_to_position(self, degrees):
        return int((degrees / 300) * 1023)
    
    def _send_command(self, servo_id, action, data):
        GPIO.output(18, GPIO.HIGH)
        command = bytearray([0xFF, 0xFF, servo_id, action, len(data) + 2]) + bytearray(data)
        command.append(self._calculate_checksum(command))
        self.port.write(command)
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(3)
    
    def _calculate_checksum(self, data):
        checksum = sum(data) & 0xFF
        return 0xFF - checksum
    
    def close(self):
        self.port.close()
        GPIO.cleanup()
