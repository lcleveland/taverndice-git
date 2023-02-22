"""
File: rolling_enging.py
Author: Lyle Cleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Controls the behavior of how dice roll.
"""

from abc import ABC, abstractmethod
import random
from dataclasses import dataclass


class RollingEngine(ABC):
    """Defines the behavior of rolling engines."""

    @abstractmethod
    def roll(self, sides: int) -> int:
        """Roll a die."""


@dataclass
class PrngRollingEngine(RollingEngine):
    """Pseudo-random engine."""

    def roll(self, sides: int) -> int:
        return random.randint(1, sides)
