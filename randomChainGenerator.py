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
# Tracking overall results.
finalResults_counts = [0, 0, 0, 0];
bySeparation_inContactResults = {};
bySeparation_notInContactResults = {};

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
    finalResults_counts[0] += results[0];
    finalResults_counts[1] += results[1];
    finalResults_counts[2] += results[2];
    finalResults_counts[3] += results[3];
    for key in results[4]:
        if key in bySeparation_inContactResults.keys():
            bySeparation_inContactResults[key] += results[4][key];
        else:
            bySeparation_inContactResults[key] = results[4][key];
    for key in results[5]:
        if key in bySeparation_notInContactResults.keys():
            bySeparation_notInContactResults[key] += results[5][key];
        else:
            bySeparation_notInContactResults[key] = results[5][key];
    print(f"Step {i}/1000 Completed")

print(f"Expected contact probability: {finalResults_counts[0]/(finalResults_counts[0] + finalResults_counts[1])},\
 Unexpected contact probability: {finalResults_counts[2]/(finalResults_counts[2] + finalResults_counts[3])}")
bySeparation_probabilities = {};
for key in bySeparation_notInContactResults:
    if key in bySeparation_inContactResults.keys():
        bySeparation_probabilities[key] = bySeparation_inContactResults[key]/(bySeparation_inContactResults[key] + bySeparation_notInContactResults[key]);
    else:
        bySeparation_probabilities[key] = 0;
print(f"Probabilties by blob overlap: {bySeparation_probabilities}")