from particle import *;
from generateParticle import *;
from populateContacts import populateContacts;
from blobProbabilities import blobProbabilities;

PARTICLE_TYPES = [G_particle, P_particle, A_particle, V_particle,\
                  L_particle, I_particle, M_particle, C_particle,\
                  F_particle, Y_particle, W_particle, H_particle,\
                  K_particle, R_particle, Q_particle, N_particle,\
                  E_particle, D_particle, S_particle, T_particle];

# The total amount that will be placed, not including the origin and
# the particle immediately after.
NUM_PARTICLES = 98;
# Tracking results.
inContactResults = {};
notInContactResults = {};
expected_inContact = 0;
expected_noContact = 0;
unexpected_inContact = 0;
unexpected_noContact = 0;

# Repeating 1000 times.
for i in range(1000):
    # Making an initial particle at the origin.
    particleType_0 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_0 = particleType_0(xCoord = 0, yCoord = 0, zCoord = 0);
    # Making a second particle right after the first one.
    particleType_1 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_0.setNext(generateParticle(particle_0, particleType_1));
    # Now that the first two particles exist, we can begin the loop to
    # create the N+2 particles relative to particle N. Beginning with
    # N = 0.
    currPar = particle_0;
    # Tracking all particles that have been made.
    particleSet = set([particle_0, particle_0.next])
    # Looping through to make N+2 particles.
    for num in range(NUM_PARTICLES):
        # Generating a random residue type.
        particleType = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
        # Generating the N+2 particle.
        nextPar = generateParticle_N2(currPar, particleType);
        # Setting N+2 to come after N+1.
        currPar.next.setNext(nextPar);
        # Adding N+2 to the particle set.
        particleSet.add(nextPar);
        # Updating the current particle to N+1.ae
        currPar = currPar.next;
    # Populating contacts for each particle.
    for par in particleSet:
        distances = populateContacts(par, particleSet);
    # Relative to each particle, find the incidence of non-contacts in a blob.
    results = blobProbabilities(particleSet);
    # Adding results to overall counters.
    inContactTmp = results[0];
    notInContactTmp = results[1];
    expected_inContact += results[2];
    unexpected_inContact += results[3];
    expected_noContact += results[4];
    unexpected_noContact += results[5];
    for key in inContactTmp:
        if key in inContactResults.keys():
            inContactResults[key] = inContactResults[key] + inContactTmp[key];
        else:
            inContactResults[key] = inContactTmp[key];
    for key in notInContactTmp:
        if key in notInContactResults.keys():
            notInContactResults[key] = notInContactResults[key] + notInContactTmp[key];
        else:
            notInContactResults[key] = notInContactTmp[key];
    print(f"Step {i + 1}/1000 Completed")
# Computing some final stats.
# 1. Calculating the contact probability by blob separation (distance - blob size).
bySeparation_contactProbabilities = {};
for key in notInContactResults:
    if key in inContactResults.keys():
        bySeparation_contactProbabilities[key] = inContactResults[key]/(inContactResults[key] + notInContactResults[key]);
    else:
        bySeparation_contactProbabilities[key] = 0;
# 2. Calculating the overall contact probability.
contactProb = (expected_inContact + unexpected_inContact)/(expected_inContact + expected_noContact + unexpected_noContact + unexpected_inContact);
# 3. Calculating the probability of a contact being within a blob (expected contact).
contact_expectedProb = expected_inContact/(expected_inContact + unexpected_inContact);
# 4. Calculating the probability of a non-contact being outside of a blob (expected non-contact).
nonContact_expectedProb = expected_noContact/(expected_noContact + unexpected_noContact);
# 5. Calculating the probability of a result going as expected according to the blob based model.
BBM_accuracy = (expected_inContact + expected_noContact)/(expected_inContact + expected_noContact + unexpected_inContact + unexpected_noContact);
# Printing Results.
print(f"Overall Contact Probability: {contactProb}");
print(f"Probability of Contact Being Expected: {contact_expectedProb}\nProbability of Non-Contact Being Expected: {nonContact_expectedProb}");
print(f"BBM Accuracy: {BBM_accuracy}");
print(f"Contact Probabilties by Blob Overlap: {bySeparation_contactProbabilities}\nIn Contact Results: {inContactResults}\nNon-Contact Results: {notInContactResults}");