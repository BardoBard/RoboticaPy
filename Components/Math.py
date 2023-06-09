import numpy


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