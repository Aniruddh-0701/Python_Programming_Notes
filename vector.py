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
        self.magnitude = sqrt(x ** 2 + y ** 2 + z ** 2)

    def dotProduct(self, obj):
        return ()

    # def __mul__(self, obj):
    #     x = self.y * obj.z - self.z * obj.y
    #     y = self.z * obj.x - self.x * obj.z
    #     z = self.x * obj.y - self.y * obj.x
    #     return Vector(x, y, z)

    # def __matmul__(self, obj):
    #     return self.x*obj.x + self.y*obj.y + self.z*obj.z

    def __repr__(self):
        x = f"i" if self.x == 1 else f"-i" if self.x == -1 else f"{self.x}i"
        y = f" +j" if self.y == 1 else f" -j" if self.y == -1 else f" {self.y:+}j"
        z = f" +k" if self.z == 1 else f" -k" if self.z == -1 else f" {self.z:+}k"
        return x + y + z


aVector = Vector(x=2, y=3, z=-1)  # 2i + 3j - k
bVector = Vector(x=1, y=10, z=-3)  # i + 10j - 3k
print(aVector)
print(aVector.magnitude)
print(aVector * bVector)
# print(aVector @ bVector)
