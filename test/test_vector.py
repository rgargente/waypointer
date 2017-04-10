import pytest

from vector import Vector


def test_from_cartesian():
    north = Vector.from_cartesian(0, 5)
    assert north.range == 5
    assert north.heading == 0
    east = Vector.from_cartesian(10, 0)
    assert east.range == 10
    assert east.heading == 90
    south = Vector.from_cartesian(0, -11)
    assert south.range == 11
    assert south.heading == 180
    west = Vector.from_cartesian(-20, 0)
    assert west.range == 20
    assert west.heading == 270
    northeast = Vector.from_cartesian(2, 2)
    assert northeast.range == pytest.approx(2.8, 0.1)
    assert northeast.heading == 45


def test_to_cartesian():
    print('\n')
    print(Vector(0, 10)._to_cartesian())
    print(Vector(90, 10)._to_cartesian())
    print(Vector(180, 10)._to_cartesian())
    print(Vector(270, 10)._to_cartesian())
    # print(Vector(45, 10)._to_cartesian())

    assert Vector(0, 10)._to_cartesian() == pytest.approx((0, 10))
    assert Vector(90, 20)._to_cartesian() == pytest.approx((20, 0))
    assert Vector(180, 30)._to_cartesian() == pytest.approx((0, -30))
    assert Vector(270, 40)._to_cartesian() == pytest.approx((-40, 0))
    assert Vector(45, 50)._to_cartesian() == pytest.approx((35.3, 35.3), 0.1)


def test_from_and_to_cartesian():
    v = Vector.from_cartesian(1, 2)
    v._to_cartesian() == (1, 2)
    v = Vector.from_cartesian(-23, 12)
    v._to_cartesian() == (-23, 12)


def test_get_course():
    waypoint_vector = Vector(90, 30)
    position_vector = Vector(90, 50)
    course = Vector.get_course(waypoint_vector, position_vector)
    assert course.heading == 270
    assert course.range == 20
