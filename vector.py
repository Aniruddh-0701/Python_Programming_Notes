# Class Vector. Stores the data of a 3d vector (Mathematical)
# Define suitable attributes and behaviour for the instances.
# Required: scalar and vector product, addition
# Optional: angle between the vectors, distance from origin, Magnitude, ...
# ai + bj + ck

from math import sqrt


class Vector(object):
    def __init__(self, /, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dotProduct(self, obj):
        return ()

    def __repr__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


aVector = Vector(x=2, y=3, z=-1)  # 2i + 3j - k
print(aVector)
print(aVector.magnitude())
