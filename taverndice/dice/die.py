"""
File: die.py
Author: Lyle Cleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Represents a die.
"""

from dataclasses import dataclass
from .rolling_engine import RollingEngine


@dataclass
class Die:
    """Represents a die."""

    sides: int
    rolling_engine: RollingEngine
