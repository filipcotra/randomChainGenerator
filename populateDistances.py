from calculateDistance import calculateDistance;

# Method to take a particle and find all of its contacts in a
# given particle set.
def populateDistances(sourcePar, particleSet):
    distances = {};
    for par in particleSet:
        if par == sourcePar:
            continue;
        distance = calculateDistance(sourcePar, par);
        distances[par] = distance;
    return distances;