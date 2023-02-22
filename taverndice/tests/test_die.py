from hypothesis import given, strategies
from ..dice.die import Die
from ..dice.rolling_engine import PrngRollingEngine


@given(strategies.integers(min_value=1))
def test_set_sides(sides):
    assert Die(sides, PrngRollingEngine()).sides == sides
