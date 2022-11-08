"""Math operations"""
from app.config import Config


class RoundingToAppConfig:
    """Round the value to app's rounding precision configuration"""
    @staticmethod
    def get_result(value):
        """Get rounding precision"""
        return round(value, Config.rounding_precision)


class SquareNum:
    """Square the number"""
    @staticmethod
    def get_square(value):
        """Get the square of a number"""
        return pow(value, 2)

