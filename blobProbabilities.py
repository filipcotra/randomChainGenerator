from findSeparation import findSeparation;

# This method will, for each particle, count how many non-contacts
# are within the blob-region.
def blobProbabilities(particleSet):
    # Counters for raw contact/non-contact data.
    expectedContact_inContact = 0;
    expectedContact_notInContact = 0;
    unexpectedContact_inContact = 0;
    unexpectedContact_notInContact = 0;
    # Counters for contacts by effective separation.
    bySeparation_inContact = {};
    bySeparation_notInContact = {};
    for particle in particleSet:
        # Finding how far each particle is from the current particle.
        separation = findSeparation(particle, particleSet);
        for parKey in separation.keys():
            if parKey == particle:
                continue;
            # If the degree of separation minus the blob size of the
            # particle falls within the blob size of the selected particle,
            # then it is an expected contact.
            effectiveSeparation = separation[parKey] - parKey.blobSize
            if effectiveSeparation <= particle.blobSize:
                if parKey in particle.getContacts():
                    expectedContact_inContact += 1;
                    if effectiveSeparation not in bySeparation_inContact.keys():
                        bySeparation_inContact[effectiveSeparation] = 1;
                    else:
                        bySeparation_inContact[effectiveSeparation] += 1;
                else:
                    expectedContact_notInContact += 1;
                    if effectiveSeparation not in bySeparation_notInContact.keys():
                        bySeparation_notInContact[effectiveSeparation] = 1;
                    else:
                        bySeparation_notInContact[effectiveSeparation] += 1;
            # This would be unexpected to be in contact.
            else:
                if parKey in particle.getContacts():
                    unexpectedContact_inContact += 1;
                    if effectiveSeparation not in bySeparation_inContact.keys():
                        bySeparation_inContact[effectiveSeparation] = 1;
                    else:
                        bySeparation_inContact[effectiveSeparation] += 1;
                else:
                    unexpectedContact_notInContact += 1;
                    if effectiveSeparation not in bySeparation_notInContact.keys():
                        bySeparation_notInContact[effectiveSeparation] = 1;
                    else:
                        bySeparation_notInContact[effectiveSeparation] += 1;
    return [expectedContact_inContact, expectedContact_notInContact,\
            unexpectedContact_inContact, unexpectedContact_notInContact,\
            bySeparation_inContact, bySeparation_notInContact]
