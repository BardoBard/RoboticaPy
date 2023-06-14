import numpy
import math

class Math:
    """
    static class for math operations
    """

    @staticmethod
    def normalize_zero(value, min_value, max_value):
        """
        normalizes a number between 0 and 1
        """
        return numpy.clip((value - min_value) / (max_value - min_value), a_min=-1, a_max=1)

    @staticmethod
    def normalize_neg(value, min_value, max_value):
        """
        normalizes a number between -1 and 1
        """
        return numpy.clip(2 * ((value - min_value) / (max_value - min_value)) - 1, a_min=-1, a_max=1)

    @staticmethod
    def rotate_tuple_over_origin(tuple_: tuple[float, float], angle) -> tuple[float, float]:
        """rotates a point over the origin

        Args:
            tuple_ (tuple): the tuple you want to rotate
            angle (_type_): the degrees you want to rotate by

        Returns:
            tuple[float, float]: a rotated tuple
        """
        angle_in_rads = math.radians(angle)
        s = math.sin(angle_in_rads)
        c = math.cos(angle_in_rads)
        
        x = tuple_[0]
        y = tuple_[1]
        
        new_x = x * c - y * s
        new_y = x * s + y * c
        
        return (new_x, new_y)
        