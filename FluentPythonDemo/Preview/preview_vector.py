from math import hypot

class Vector:

    def __init__(self, x=0, y=0) -> None:
        self.m_X = x
        self.m_Y = y

    def __repr__(self) -> str:
        return 'Vector(%r, %r)' % (self.m_X, self.m_Y)

    def __abs__(self):
        return hypot(self.m_X, self.m_Y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.m_X + other.m_X, self.m_Y + other.m_Y)
    
    def __mul__(self, scalar):
        return Vector(self.m_X * scalar, self.m_Y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v3 = Vector(3, 4)
print(abs(v3))

print(abs(v3 * 3))