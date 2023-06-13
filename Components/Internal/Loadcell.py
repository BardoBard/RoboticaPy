from hx711 import HX711

class CustomHX711:
    def __init__(self, dout_pin, pd_sck_pin):
        self.hx = HX711(dout_pin, pd_sck_pin)

    def setup(self):
        self.hx.set_reading_format("MSB", "MSB")
        self.hx.set_reference_unit(1)
        self.hx.reset()
        self.hx.tare()

    def get_weight(self, num_readings=5):
        return self.hx.get_weight_mean(num_readings)


def main():
    hx711 = CustomHX711(dout_pin=16, pd_sck_pin=20)
    hx711.setup()

    try:
        while True:
            weight = hx711.get_weight()
            print(f"Weight: {weight} g")
    except KeyboardInterrupt:
        hx711.power_down()


if __name__ == "__main__":
    main()