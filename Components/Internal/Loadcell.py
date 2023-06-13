import RPi.GPIO as GPIO
import time


class HX711:
    def __init__(self, dout_pin, pd_sck_pin):
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dout_pin, GPIO.IN)
        GPIO.setup(self.pd_sck_pin, GPIO.OUT)
        GPIO.output(self.pd_sck_pin, GPIO.LOW)

        self.offset = 0
        self.scale = 1

    def __del__(self):
        GPIO.cleanup()

    def get_value(self, num_readings=10):
        """
        Read the average value from the load cell.

        Args:
            num_readings (int): Number of readings to average (default: 10).

        Returns:
            float: Scaled value in the desired unit.
        """
        sum_values = 0
        for _ in range(num_readings):
            sum_values += self.read()
            time.sleep(0.01)

        average_value = sum_values / num_readings
        scaled_value = (average_value - self.offset) / self.scale
        return scaled_value

    def tare(self, num_readings=10):
        """
        Perform tare operation to calculate the offset.

        Args:
            num_readings (int): Number of readings to average (default: 10).
        """
        sum_values = 0
        for _ in range(num_readings):
            sum_values += self.read()
            time.sleep(0.01)

        self.offset = sum_values / num_readings

    def set_scale(self, scale):
        """
        Set the scale value to convert raw readings to desired units.

        Args:
            scale (float): Scale value.
        """
        self.scale = scale

    def read(self):
        """
        Read raw data from the load cell.

        Returns:
            int: Raw data from the load cell.
        """
        while GPIO.input(self.dout_pin):
            pass

        data_bits = []
        for _ in range(24):
            GPIO.output(self.pd_sck_pin, GPIO.HIGH)
            data_bits.append(GPIO.input(self.dout_pin))
            GPIO.output(self.pd_sck_pin, GPIO.LOW)

        GPIO.output(self.pd_sck_pin, GPIO.HIGH)
        GPIO.output(self.pd_sck_pin, GPIO.LOW)

        data_bits = data_bits[::-1]
        data_bits.append(0)

        value = 0
        for bit in data_bits:
            value = (value << 1) | bit

        return value


def main():
    GPIO.setwarnings(False)

    # GPIO pin numbers for the HX711 module
    dout_pin = 16
    pd_sck_pin = 20

    # Create an instance of the HX711 class
    hx711 = HX711(dout_pin, pd_sck_pin)

    # Perform tare operation to calculate the offset
    hx711.tare()

    # Read the weight from the load cell continuously
    try:
        while True:
            weight = hx711.get_value()
            print(f"Weight: {weight:.2f} kg")
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
