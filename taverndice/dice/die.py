"""
File: die.py
Author: Lyle Cleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Represents a die.
"""


from dataclasses import dataclass

@dataclass
class Die:
    """Represents a die."""
    sides: int
