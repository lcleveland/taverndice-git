from hypothesis import given, strategies
import pytest
from ..dice.die import Die
from ..dice.rolling_engine import PrngRollingEngine
from ..dice.exceptions import InvalidDieSidesException


@given(strategies.integers(min_value=2, max_value=1000))
def test_set_sides(sides):
    assert Die(sides, PrngRollingEngine()).sides == sides


@given(strategies.integers(min_value=-1, max_value=1))
def test_sides_not_less_than_two(sides):
    with pytest.raises(InvalidDieSidesException):
        Die(sides, PrngRollingEngine()).sides = sides
