import numpy as np
import math


class Vector:
    def __init__(self, heading, range):
        self.heading = heading
        """Heading in degrees. 0 = north, 90=east, 180=south, 270=west"""
        self.range = range
        """In any distance unit"""

    @classmethod
    def from_cartesian(cls, x, y):
        heading = math.degrees(np.arctan2(y, x) - math.pi / 2)  # -pi/2 because 0 must point north
        if heading != 0: heading *= -1  # we want to move clockwise
        if heading < 0: heading += 360  # always show angles in positive numbers
        range = np.sqrt(x ** 2 + y ** 2)
        return cls(heading, range)

    @classmethod
    def get_course(cls, waypoint_vector, position_vector):
        course = np.array(waypoint_vector._to_cartesian()) - np.array(position_vector._to_cartesian())
        return cls.from_cartesian(*course)

    def _to_cartesian(self):
        # We make the opposite changes as in from_cartesian
        rad = math.radians(self.heading) * (-1)
        rad += math.pi / 2
        x = self.range * np.cos(rad)
        y = self.range * np.sin(rad)
        return (x, y)
