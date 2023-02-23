from hypothesis import given, strategies
import pytest
from ..dice.die import Die
from ..dice.rolling_engine import PrngRollingEngine
from ..dice.exceptions import InvalidDieSidesException


@given(strategies.integers(min_value=2, max_value=1000))
def test_set_sides(sides):
    assert Die(PrngRollingEngine(), sides).sides == sides


@given(strategies.integers(min_value=-1, max_value=1))
def test_sides_not_less_than_two(sides):
    with pytest.raises(InvalidDieSidesException):
        Die(PrngRollingEngine(), sides).sides = sides


@given(strategies.integers(min_value=2, max_value=10000))
def test_die_roll(sides):
    assert 2 <= Die(PrngRollingEngine(), sides).roll() <= 10000
