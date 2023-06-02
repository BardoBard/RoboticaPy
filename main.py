from Components.Internal.Bluetooth import Bluetooth

def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(':)')
    bluetooth = Bluetooth()
    bluetooth.scan()
    controller_mac_address = "78:21:84:7C:A4:F6"
    bluetooth.connect(controller_mac_address)
