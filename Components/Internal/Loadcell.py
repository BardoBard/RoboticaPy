from hx711 import HX711
import RPi.GPIO as GPIO

class Loadcell:

    __init__ = None

    hx711 = HX711(
        dout_pin=16,
        pd_sck_pin=20
    )

    # This function returns a list of 5 measures
    def get_weight():
        try:
            hx711.reset()   # Before we start, reset the HX711 (not obligate)
            measures = hx711.get_raw_data(num_measures=5)
        finally:
            GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
        return measures

if __name__ == '__main__':
    measures = get_weight()
    print(measures)
