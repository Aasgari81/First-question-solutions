from math import pi

class circle:

    def __init__ (self, r):
        if not isinstance(r, int) and not isinstance(r, float):
            raise TypeError('Radius must be float or integer')
        self.radius = r
    def getarea(self):
        return pi*self.radius**2
    def getperimeter(self):
        return pi*self.radius*2

