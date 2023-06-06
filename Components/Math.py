class Math:
    """
    static class for math operations
    """

    @staticmethod
    def normalize(value, min_value, max_value):
        return (value - min_value) / (max_value - min_value)

    @staticmethod
    def normalize_neg_one(value, min_value, max_value):
        return 2((value - min_value) / (max_value - min_value)) - 1
