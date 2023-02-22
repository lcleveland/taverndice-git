"""
File: rolling_enging.py
Author: Lyle Cleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Controls the behavior of how dice roll.
"""

from abc import ABC, abstractmethod


class RollingEngine(ABC):
    """Defines the behavior of rolling engines."""

    @abstractmethod
    def roll(self, sides: int) -> int:
        """Roll a die."""
