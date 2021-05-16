# Class Vector. Stores the data of a 3d vector (Mathematical)
# Define suitable attributes and behaviour for the instances.
# Required: scalar// and vector// product, addition//
# Optional: angle between the vectors //, distance from a point, Magnitude//, ...
# ai + bj + ck

from math import sqrt, acos


class Vector(object):
    # Vector initialization
    def __init__(self, /, x=0, y=0, z=0):
        self.x = x  # Distance along x-axis
        self.y = y  # Distance along y-axis
        self.z = z  # Distance along z-axis
        self.magnitude = sqrt(x ** 2 + y ** 2 + z ** 2)  # Magnitude of vector
    
    # Vector Addition
    def add(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        z = self.z + obj.z
        return Vector(x, y, z)
    
    def __add__(self, obj):
        x = self.x + obj.x
        y = self.y + obj.y
        z = self.z + obj.z
        return Vector(x, y, z)

    # Scalar Product
    def dotProduct(self, obj):
        return self.x*obj.x + self.y*obj.y + self.z*obj.z

    def __matmul__(self, obj):  # Overriding builtin method for @
        return self.x*obj.x + self.y*obj.y + self.z*obj.z

    # Vector Product
    def crossProduct(self, obj):
        x = self.y * obj.z - self.z * obj.y
        y = self.z * obj.x - self.x * obj.z
        z = self.x * obj.y - self.y * obj.x
        return Vector(x, y, z)

    def __mul__(self, obj):  # Overriding builtin method for *
        x = self.y * obj.z - self.z * obj.y
        y = self.z * obj.x - self.x * obj.z
        z = self.x * obj.y - self.y * obj.x
        return Vector(x, y, z)

    # String representation of vector
    def __repr__(self):
        x = (
            f"i\u0302" if self.x == 1 else f"-i\u0302" if self.x == -1 else f"{self.x}i\u0302"
        )
        y = (
            f" +j\u0302"
            if self.y == 1
            else f" -j\u0302"
            if self.y == -1
            else f" {self.y:+}j\u0302"
        )
        z = (
            f" +k\u0302"
            if self.z == 1
            else f" -k\u0302"
            if self.z == -1
            else f" {self.z:+}k\u0302"
        )
        return x + y + z

    # Angle between vectors
    def vectorAngle(self, obj):
        angle = self @ obj / (self.magnitude * obj.magnitude)
        return acos(angle)

print()
aVector = Vector(x=2, y=3, z=-1)  # 2i + 3j - k
bVector = Vector(x=1, y=10, z=-3)  # i + 10j - 3k

print(aVector, aVector.magnitude)
print(bVector, bVector.magnitude)

# Dot Product execution
print(f'\n{aVector.dotProduct(bVector)}')
print(aVector @ bVector)

# Cross Product Execution
print(f'\n{aVector.crossProduct(bVector)}')
print(aVector * bVector)

# Addition
print(f'\n{aVector.add(bVector)}')
print(aVector+bVector)

# Angle between vectors
print(f'\n{aVector.vectorAngle(bVector)} rad')
