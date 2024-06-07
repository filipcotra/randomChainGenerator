from calculateDistance import calculateDistance;

# Defining contact distance limit as being 6 angstroms.
CONTACT_LIMIT = 6;

# Method to take a particle and find all of its contacts in a
# given particle set.
def populateContacts(sourcePar, particleSet):
    distances = {};
    for par in particleSet:
        if par == sourcePar:
            continue;
        distance = calculateDistance(sourcePar, par);
        distances[par] = distance;
        if distance < CONTACT_LIMIT:
            sourcePar.addContact(par);
    return distances;