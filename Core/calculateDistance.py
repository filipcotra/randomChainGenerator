import math;

# Calculating 3D distance between two particles.
def calculateDistance(particleA, particleB):
    xDiff = particleB.xCoord - particleA.xCoord;
    yDiff = particleB.yCoord - particleA.yCoord;
    zDiff = particleB.zCoord - particleA.zCoord;
    return math.sqrt(xDiff**2 + yDiff**2 + zDiff**2);