import sys
import RPi.GPIO as GPIO
from hx711 import HX711

class Loadcell:
    def __init__(self, dout_pin, pd_sck_pin, reference_unit):
        self.hx = HX711(dout_pin, pd_sck_pin)
        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(reference_unit)
        self.hx.reset()
        self.hx.tare()
        print("Tare done! Add weight now...")

    def get_weight(self):
        """
        Returns the average weight over 5 readings
        """
        return self.hx.get_weight(5)  # Get the average weight over 5 readings

    def tare(self):
        """
        Resets the scale to 0
        """
        self.hx.tare()

    def set_reference_unit(self, reference_unit):
        """
        Sets the reference unit
        """
        self.hx.set_reference_unit(reference_unit)

    def power_down(self):
        self.hx.power_down()

    def power_up(self):
        self.hx.power_up()

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

def calculate_reference_unit():
    dout_pin = 16
    pd_sck_pin = 20

    # Create an instance of the HX711 class
    hx = HX711(dout_pin, pd_sck_pin)

    # Set the reference unit to an initial value of 1
    hx.set_reference_unit(1)

    # Calibrate the loadcell
    hx.reset()  # Reset the HX711
    hx.tare()   # Tare the loadcell 

    # Prompt the user to place a known weight on the loadcell
    input("Place a known weight on the cell and press enter to continue...")

    # Read the average value from the HX711 over multiple readings
    average_value = hx.get_raw_data_mean()

    # Prompt the user to enter the weight of the known object
    known_weight = float(input("Enter the weight of the known object (in your desired unit): "))

    # Calculate the reference unit
    reference_unit = average_value / known_weight

    # Print the calculated reference unit
    print("Reference Unit: {:.2f}".format(reference_unit))

    # Cleanup GPIO pins
    GPIO.cleanup()

if __name__ == "__main__":
    # Prompt the user to calibrate the loadcell, or start measuring
    calibrate = input("Calibrate loadcell? (y/n): ")

    # If the user wants to calibrate the loadcell
    if calibrate == "y":
        calculate_reference_unit()
    else:
        # Create an instance of the Loadcell class
        loadcell = Loadcell(16, 20, 1)

        # Start measuring the weight
        while True:
            try:
                print(loadcell.get_weight())
            except (KeyboardInterrupt, SystemExit):
                cleanAndExit()
