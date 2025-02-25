from Core.calculateDistance import calculateDistance;

# Defining contact distance limit as being 6 angstroms.
CONTACT_LIMIT = 6;

# Purpose: To take a particle and find all of its contacts from
# a given set of existing particles. Updating contactSet with sets
# containing the two contacting particles.
# Parameters:
#   sourcePar = The source particle.
#   particleSet = The set of all existing particles.
def populateContacts(sourcePar, particleSet, contactSet):
    distances = {};
    # Looping through each particle, which is a potential contact.
    for par in particleSet:
        if par == sourcePar:
            continue;
        # Calculating euclidean distance.
        distance = calculateDistance(sourcePar, par);
        distances[par] = distance;
        # If the two particles are within 6 angstroms of one another,
        # they are in contact.
        if distance < CONTACT_LIMIT:
            potentialVal = frozenset([sourcePar, par]);
            # If the potential value is already in the contact set, don't assign it again.
            if not potentialVal in contactSet:
                contactSet.add(potentialVal);