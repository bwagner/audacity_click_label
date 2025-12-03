import pytest
import math

from audacity_click_label import acl


def test1():
    acl1 = acl()
    assert next(acl1) == 0
    assert next(acl1) == 1
    assert next(acl1) == 2


def test2():
    acl1 = acl(7, 2)
    assert next(acl1) == 0
    assert next(acl1) == 2
    assert next(acl1) == 4
    assert next(acl1) == 6
    with pytest.raises(StopIteration):
        assert next(acl1) == 8


def test3():
    with pytest.raises(ValueError):
        acl1 = acl(-7, -2)
        assert next(acl1) == 0  # without this line, acl1 is not even instantiated


def test4():
    incr = 1.43
    acl1 = acl(7, incr)
    assert next(acl1) == 0
    assert next(acl1) == incr
    assert next(acl1) == 2 * incr
    assert next(acl1) == 3 * incr


def test5():
    incr = 1.43
    start = 1.53
    acl1 = acl(7, incr, start)
    assert math.isclose(next(acl1), start)
    assert math.isclose(next(acl1), start + incr)
    assert math.isclose(next(acl1), start + 2 * incr)
    assert math.isclose(next(acl1), start + 3 * incr)
