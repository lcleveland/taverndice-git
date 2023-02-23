"""
File: die.py
Author: Lyle Cleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Represents a die.
"""

from dataclasses import dataclass
from .rolling_engine import RollingEngine
from .exceptions import InvalidDieSidesException


@dataclass
class Die:
    """Represents a die."""
    _sides: int

    @property
    def sides(self) -> int:
        return self._sides

    @sides.setter
    def sides(self, value: int) -> None:
        if value <= 1:
            raise InvalidDieSidesException("Sides must be greater than 1")
        self._sides = value

    rolling_engine: RollingEngine

    def roll(self) -> int:
        """Roll the die using the rolling engine and return the result."""
        return self.rolling_engine.roll(self.sides)
