from calculateDistance import calculateDistance;

# Defining contact distance limit as being 6 angstroms.
CONTACT_LIMIT = 6;
# Tracking the contact set key. This number is essentially
# meaningless.
contactKey = 0;

# Method to take a particle and find all of its contacts in a
# given particle set.
def populateContacts(sourcePar, particleSet, contactSet):
    global contactKey;
    distances = {};
    for par in particleSet:
        if par == sourcePar:
            continue;
        distance = calculateDistance(sourcePar, par);
        distances[par] = distance;
        if distance < CONTACT_LIMIT:
            # Not actually adding contacts as we want to add them randomly.
            # For now, only recording that they exist and thus should be added
            # later in some random order. Also ensuring that each contact is
            # only recorded once.
            potentialVal = set([sourcePar, par]);
            if not any(potentialVal == contactSet[x] for x in contactSet.keys()):
                contactSet[contactKey] = set([sourcePar, par]);
                contactKey += 1;
    return contactSet;