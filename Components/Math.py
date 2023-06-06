class Math:
    """
    static class for math operations
    """

    @staticmethod
    def normalize(value, min_value, max_value):
        return (value - min_value) / (max_value - min_value)
