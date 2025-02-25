import pandas as pd;
from Particle.particle import *;
from Particle.generateParticle import *;
from Particle.populateContacts import populateContacts;
from Core.findSeparation import findSeparation;
from HandleIO.printBlobInfo import printDf;

PARTICLE_TYPES = [G_particle, P_particle, A_particle, V_particle,\
                  L_particle, I_particle, M_particle, C_particle,\
                  F_particle, Y_particle, W_particle, H_particle,\
                  K_particle, R_particle, Q_particle, N_particle,\
                  E_particle, D_particle, S_particle, T_particle];

# The total amount that will be placed, not including the origin and
# the particle immediately after. The real amount of particles will be
# this number + 2.
NUM_PARTICLES = 98;
# The total number of times the simulation will be run.
SIM_STEPS = 1000;
# Defining column names for data frame.
COL_NAMES = ["COUNT"];
# Tracking blob based stats.
contactsByRawSeparation = pd.DataFrame(columns = COL_NAMES);
contactsByBlobSeparation = pd.DataFrame(columns = COL_NAMES);

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
    par_N = particle_0;
    # Tracking all particles that have been made.
    particleSet = {particle_0, particle_0.next}
    # Looping through to make N+2 particles.
    for num in range(NUM_PARTICLES):
        # Generating a random residue type.
        particleType = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
        # Generating the N+2 particle.
        par_N2 = generateParticle_N2(par_N, particleType);
        # Setting N+2 to come after N+1.
        par_N.next.setNext(par_N2);
        # Adding N+2 to the particle set.
        particleSet.add(par_N2);
        # Updating the current particle to N+1.
        # N = N + 1.
        par_N = par_N.next;
        # Adding contacts between N and N+1.
        par_N.addContact(par_N.next);
        par_N.next.addContact(par_N);
    # Tracking the set of contacts that each particle has
    # without assigning contacts to that particle. This set
    # will contain sets indicating two particles that are in
    # contact with one another.
    contactSet = set();
    # Populating contacts for each particle.
    for par in particleSet:
        populateContacts(par, particleSet, contactSet);
    # Randomly adding contacts and collecting resulting stats until
    # all the steps have been completed.
    numContacts = len(contactSet); # The total number of contacts in the random chain.
    for contact in range(numContacts):
        # Randomly selecting a contact from the existing set.
        selectedContact = rand.sample(list(contactSet), 1)[0];
        newContact = list(selectedContact);
        par1, par2 = newContact[0], newContact[1];
        separation = findSeparation(par1, particleSet);
        par2_separation = separation[par2];
        # Gathering raw separation information.
        if par2_separation in contactsByRawSeparation.index:
            contactsByRawSeparation.at[par2_separation, "COUNT"] += 1;
        else:
            contactsByRawSeparation.loc[par2_separation] = 1;
        # Gathering blob probability information.
        par2_blobSeparation = par2_separation - par2.blobSize - par1.blobSize;
        if par2_blobSeparation in contactsByBlobSeparation.index:
            contactsByBlobSeparation.at[par2_blobSeparation, "COUNT"] += 1;
        else:
            contactsByBlobSeparation.loc[par2_blobSeparation] = 1;
        # Making the contact in the particle set and removing
        # it from further consideration. This is done last
        # to only impact future steps.
        par1.addContact(par2);
        par2.addContact(par1);
        contactSet.remove(selectedContact);
    print(f"Step {step + 1}/{SIM_STEPS} Completed");
# Writing data to files.
# Raw separation.
rawSorted = contactsByRawSeparation.sort_index();
rawFile = "rawSep";
printDf(rawSorted, rawFile);
# Blob separation.
blobSorted = contactsByBlobSeparation.sort_index();
blobFile = "blobSep";
printDf(blobSorted, blobFile);
# Modifying blob probability frame.
indexList = list(blobSorted.index);
index_0 = indexList.index(0);
blobSorted_filtered = blobSorted.loc[indexList[index_0:]]; # All values from 0 onwards.
blobSorted_filtered.loc[0, "COUNT"] = sum(blobSorted.loc[indexList[0 : index_0 + 1], "COUNT"]);
blobProb = blobSorted_filtered.div(blobSorted_filtered.sum(axis = 0), axis = 1); # Probability distribution for each sector
# Printing blob probability frame.
blobProbFile = "blobProb";
printDf(blobProb, blobProbFile);