"""
File: roll.py
Author: lcleveland
Email: lyle.cleveland@yahoo.com
Github: https://github.com/lcleveland
Description: Handles rolling dice.
"""
from dataclasses import dataclass, field


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
}

COMPARISON_MODES = {
    "none": 0,
    "greater_than": 1,
    "less_than": 2,
    "greater_or_equal": 3,
    "less_or_equal": 4,
}

SUCCESS_MODES = {
    "none": 0,
    "success": 1,
    "failure": 2,
}


@dataclass
class Roll:
    dice_sides: int
    dice_count: int = field(default=1)
    dice_modifier: int = field(default=0)
    modifier: int = field(default=0)
    result: int = field(init=False, default=0)
    mode: int = field(default=ROLL_MODES["none"])
    comparison_mode: int = field(default=COMPARISON_MODES["none"])
    target_numbers: list[int] = field(default_factory=list)
    success_mode: int = field(default=SUCCESS_MODES["none"])
    success_comparison_mode: int = field(default=COMPARISON_MODES["none"])
    success_targets: list[int] = field(default_factory=list)
