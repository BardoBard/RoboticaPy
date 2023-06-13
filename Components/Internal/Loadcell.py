import time
from hx711 import HX711

class WeightSensor:
    def __init__(self, dout_pin, pd_sck_pin, reference_unit=1):
        self.hx = HX711(dout_pin, pd_sck_pin)
        self.reference_unit = reference_unit

    def calibrate(self, calibration_factor):
        """
        Calibrate the sensor
        :param (int) calibration_factor: calibration factor
        :return: void
        """
        self.hx.set_scale(calibration_factor)

    def tare(self, num_samples=10):
        """
        Tare the sensor
        :param (int) num_samples: number of samples
        :return: void
        """
        self.hx.tare(num_samples)

    def get_weight(self):
        """
        Get the current weight
        :return: weight
        """
        return self.hx.get_weight(5)

    def get_weight_mean(self, num_samples=5):
        """
        Get the current weight mean
        :param (int) num_samples: number of samples
        :return: weight mean
        """
        return self.hx.get_weight_mean(num_samples)

    def power_down(self):
        self.hx.power_down()

    def power_up(self):
        self.hx.power_up()


if __name__ == '__main__':
    dout_pin = 16  # DOUT 
    pd_sck_pin = 20  # PD_SCK 

    weight_sensor = WeightSensor(dout_pin, pd_sck_pin)

    # Calibrate the sensor
    calibration_factor = 1000  # Adjust this
    weight_sensor.calibrate(calibration_factor)

    # Tare
    weight_sensor.tare()

    # Get the current weight
    weight = weight_sensor.get_weight()
    print(f"Current weight: {weight} grams")

    # Power down the sensor
    weight_sensor.power_down()

    # Wait for some time
    time.sleep(5)

    # Power up the sensor again
    weight_sensor.power_up()

    # Get the weight after powering up
    weight = weight_sensor.get_weight()
    print(f"Weight after powering up: {weight} grams")