from particle import *;
from generateParticle import *;
from populateContacts import populateContacts;
from findSeparation import findSeparation;
import random as rand;

PARTICLE_TYPES = [G_particle, P_particle, A_particle, V_particle,\
                  L_particle, I_particle, M_particle, C_particle,\
                  F_particle, Y_particle, W_particle, H_particle,\
                  K_particle, R_particle, Q_particle, N_particle,\
                  E_particle, D_particle, S_particle, T_particle];

# The total amount that will be placed, not including the origin and
# the particle immediately after.
NUM_PARTICLES = 98;
# The total number of times the simulation will be run.
SIM_STEPS = 1000;
# Tracking blob based stats.
contactsByRawSeparation = {};
contactsByBlobSeparation = {};

# Repeating 1000 times.
for step in range(SIM_STEPS):
    # Making an initial particle at the origin.
    particleType_0 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_0 = particleType_0(xCoord = 0, yCoord = 0, zCoord = 0);
    # Making a second particle right after the first one.
    particleType_1 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_0.setNext(generateParticle(particle_0, particleType_1));
    # Adding contacts between the two particles.
    particle_0.addContact(particle_0.next);
    particle_0.next.addContact(particle_0);
    # Now that the first two particles exist, we can begin the loop to
    # create the N+2 particles relative to particle N. Beginning with
    # N = 0.
    currPar = particle_0;
    # Tracking all particles that have been made.
    particleSet = set([particle_0, particle_0.next])
    # Tracking all contacts that exist.
    contactSet = {};
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
        # Updating the current particle to N+1.
        currPar = currPar.next;
        # Adding contacts between N+1 and N+2.
        currPar.addContact(currPar.next);
        currPar.next.addContact(currPar);
    # Populating contacts for each particle.
    for par in particleSet:
        contactSet = populateContacts(par, particleSet, contactSet);
    # Randomly adding contacts and collecting resulting stats until
    # all the steps have been completed.
    numContacts = len(contactSet);
    keySelection = None;
    for contact in range(numContacts):
        # Randomly selecting a contact from the existing set.
        keySelection = rand.choice(list(contactSet.keys()));
        newContact = list(contactSet[keySelection]);
        par1, par2 = newContact[0], newContact[1];
        # Gathering blob probability information based on the
        # two contacts.
        separation = findSeparation(par1, particleSet);
        par2_separation = separation[par2];
        if par2_separation in contactsByRawSeparation.keys():
            contactsByRawSeparation[par2_separation] += 1;
        else:
            contactsByRawSeparation[par2_separation] = 1;
        par2_blobSeparation = par2_separation - par2.blobSize - par1.blobSize;
        if par2_blobSeparation in contactsByBlobSeparation.keys():
            contactsByBlobSeparation[par2_blobSeparation] += 1;
        else:
            contactsByBlobSeparation[par2_blobSeparation] = 1;
        # Making the contact in the particle set and removing
        # it from further consideration. This is done last so as
        # to only impact future steps.
        par1.addContact(par2);
        par2.addContact(par1);
        contactSet.pop(keySelection);
    print(f"Step {step + 1}/{SIM_STEPS} Completed");
# Writing raw separation data to file.
rawSepItems = sorted(contactsByRawSeparation.items());
rawFile = open(f"/Users/filipcotra/Desktop/contactsByRawSeparation_{SIM_STEPS}.tsv", "w");
for rawItem in rawSepItems:
    rawFile.write(f"{rawItem[0]}\t{rawItem[1]}\n");
rawFile.close();
# Writing blob separation data to file.
blobSepItems = sorted(contactsByBlobSeparation.items());
blobFile = open(f"/Users/filipcotra/Desktop/contactsByBlobSeparation_{SIM_STEPS}.tsv", "w");
for blobItem in blobSepItems:
    blobFile.write(f"{blobItem[0]}\t{blobItem[1]}\n");
blobFile.close();