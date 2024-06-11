from findSeparation import findSeparation;

# This method will, for each particle, count how many non-contacts
# are within the blob-region.
def blobProbabilities(particleSet):
    # Counters for contacts by effective separation.
    inContact = {};
    notInContact = {};
    expected_inContact = 0; # Particles that are expected to be in contact and are.
    expected_noContact = 0; # Particles that are expected not to be in contact and are not.
    unexpected_inContact = 0; # Particles that are expected not to be in contact but are.
    unexpected_noContact = 0; # Particles that are expected to be in contact but are not.
    for particle in particleSet:
        # Finding how far each particle is from the current particle.
        separation = findSeparation(particle, particleSet);
        for parKey in separation.keys():
            if parKey == particle:
                continue;
            # If the degree of separation minus the blob size of the
            # particle falls within the blob size of the selected particle,
            # then it is an expected contact. Calculating the overlap between
            # the blobs here.
            trueSeparation = separation[parKey] - parKey.blobSize;
            if parKey in particle.getContacts():
                if trueSeparation <= particle.blobSize:
                    expected_inContact += 1; # Would expect to be in contact and is.
                else:
                    unexpected_inContact += 1; # Would expect not to be in contact bus is.
                if trueSeparation not in inContact.keys():
                    inContact[trueSeparation] = 1;
                else:
                    inContact[trueSeparation] = inContact[trueSeparation] + 1;
            else:
                if trueSeparation <= particle.blobSize:
                    unexpected_noContact += 1; # Would expect to be in contact but isn't.
                else:
                    expected_noContact += 1; # Would expect not to be in contact and isn't.
                if trueSeparation not in notInContact.keys():
                    notInContact[trueSeparation] = 1;
                else:
                    notInContact[trueSeparation] = notInContact[trueSeparation] + 1;
    return [inContact, notInContact,\
            expected_inContact, unexpected_inContact, expected_noContact, unexpected_noContact];
