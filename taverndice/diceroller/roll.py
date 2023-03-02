"""
File: roll.py
Author: lcleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Handles rolling dice.
"""
from dataclasses import dataclass, field
from ..dice.die import Die


ROLL_MODES = {
    "none": 0,
    "keep_lowest": 1,
    "keep_highest": 2,
    "drop_lowest": 3,
    "drop_highest": 4,
    "reroll_once": 5,
    "reroll_always": 6,
    "exploding": 7,
    "compounding": 8,
    "penetrating": 9,
    "successes": 10,
    "failures": 11,
}

COMPARISON_MODES = {
    "none": 0,
    "greater_than": 1,
    "less_than": 2,
    "greater_or_equal": 3,
    "less_or_equal": 4,
}


@dataclass
class Roll:
    """Roll a number of dice according to a selected mode."""

    die: Die
    """Die to roll."""

    dice_count: int = field(default=1)
    """Number of times to roll the die."""

    modifier: int = field(default=0)
    """Modifier to add to the roll total."""

    mode: int = field(default=ROLL_MODES["none"])
    """Mode used to determine how to roll the dice."""

    comparison_mode: int = field(default=COMPARISON_MODES["none"])
    """Mode used to determine any comparisons that need to be done."""

    comparison_numbers: list[int] = field(default_factory=list)
    """Numbers that are used for comparison."""
