import json

class TelemetryData:
    def __init__(self):
        self.__image_data_code = None
        self.__image_data_found = None
        self.__direction = None
        self.__arm_direction = None
        self.__ultra_sonic_data = None
        self.__updated = False

    def is_modified(self):
        return self.__updated

    # getters and setters
    def get_image_data_code(self):
        return self.__image_data_code

    def set_image_data_code(self, image_data_code):
        # if the value is the same as the current value then return
        if image_data_code is self.__image_data_code:
            return
        self.__image_data_code = image_data_code
        self.__updated = True

    def get_image_data_found(self):
        return self.__image_data_found

    def set_image_data_found(self, image_data_found):
        # if the value is the same as the current value then return
        if image_data_found is self.__image_data_found:
            return
        self.__image_data_found = image_data_found
        self.__updated = True

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        # if the value is the same as the current value then return
        if direction is self.__direction:
            return
        self.__direction = direction
        self.__updated = True

    def get_arm_direction(self):
        return self.__arm_direction

    def set_arm_direction(self, arm_direction):
        # if the value is the same as the current value then return
        if arm_direction is self.__arm_direction:
            return
        self.__arm_direction = arm_direction
        self.__updated = True

    def get_ultra_sonic_data(self):
        return self.__ultra_sonic_data

    def set_ultra_sonic_data(self, ultra_sonic_data):
        # if the value is the same as the current value then return
        if ultra_sonic_data is self.__ultra_sonic_data:
            return
        self.__ultra_sonic_data = ultra_sonic_data
        self.__updated = True

    # convert to json
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == '__main__':
    # test
    telemetry_data = TelemetryData()
    telemetry_data.set_image_data_code("a code")
    telemetry_data.set_image_data_found("True")
    telemetry_data.set_direction("forward")
    telemetry_data.set_arm_direction("up")
    telemetry_data.set_ultra_sonic_data("19.5cm")
    print(telemetry_data.to_json())