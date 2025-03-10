import math

class Sphere(object):
    def __init__(self, radius, mass):
        self._radius = radius
        self._mass = mass

    def getRadius(self):
        return self._radius

    def getMass(self):
        return self._mass

    def getVolume(self):
        volume = (4/3) * math.pi * self._radius ** 3
        return round(volume, 5)

    def getSurfaceArea(self):
        surfaceArea = 4 * math.pi * self._radius ** 2
        return round(surfaceArea, 5)

    def getDensity(self):
        volume = (4/3) * math.pi * self._radius ** 3
        density = self._mass / volume
        return round(density, 5)
    
ball = Sphere(2, 50)
print(ball.getRadius())     
print(ball.getMass())         
print(ball.getVolume())      
print(ball.getSurfaceArea())  
print(ball.getDensity())  