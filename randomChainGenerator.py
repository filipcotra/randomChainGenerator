from particle import *;
from generateParticle import *;
from populateDistances import populateDistances;

PARTICLE_TYPES = [G_particle, P_particle, A_particle, V_particle,\
                  L_particle, I_particle, M_particle, C_particle,\
                  F_particle, Y_particle, W_particle, H_particle,\
                  K_particle, R_particle, Q_particle, N_particle,\
                  E_particle, D_particle, S_particle, T_particle];

# Defining contact distance limit as being 6 angstroms.
CONTACT_LIMIT = 2;
# Tracking results.
contactExpected = 0;
not_contactExpected = 0;
# Tracking separation.
contactExpected_bySep = {};
not_contactExpected_bySep = {};

# Repeating 10,000 times.
for i in range(10000):
    # Boolean to track if a contact has occurred.
    contactMade = False;
    # Making an initial particle at the origin.
    particleType_0 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_0 = particleType_0(xCoord = 0, yCoord = 0, zCoord = 0);
    # Making a second particle right after the first one.
    particleType_1 = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
    particle_1 = generateParticle(particle_0, particleType_1)
    # Setting up the links between them.
    particle_0.setNext(particle_1);
    # Now that the first two particles exist, we can begin the loop to
    # create the N+2 particles relative to particle N. Beginning with
    # N = 0.
    currPar = particle_0;
    # Tracking all particles that have been made.
    particleSet = [particle_0, particle_1];
    # Looping through to make N+2 particles.
    while not contactMade:
        # Generating a random residue type.
        particleType = PARTICLE_TYPES[rand.randint(0, len(PARTICLE_TYPES) - 1)];
        # Generating the N+2 particle.
        nextPar = generateParticle_N2(currPar, particleType);
        # Setting N+2 to come after N+1.
        currPar.next.setNext(nextPar);
        # Adding N+2 to the particle set.
        particleSet.append(nextPar);
        # Updating the current particle to N+1.
        currPar = currPar.next;
        # Checking to see if a contact exists between any existing particles.
        for par in particleSet:
            distances = populateDistances(par, particleSet);
            for distantPar in distances.keys():
                sequenceSeparation = particleSet.index(distantPar) - particleSet.index(par);
                # If the distance is within contact distance but not equivalent
                # to the expected bond between two particles, it is a contact.
                if distances[distantPar] <= CONTACT_LIMIT and sequenceSeparation > 2:
                    contactMade = True;
                    # par1 will always be earlier in sequence than par2.
                    par1 = par;
                    par2 = distantPar;
                    par2_separation = sequenceSeparation;
                    break;
            if contactMade:
                break;
    # Calculate the blob separation of these particles.
    trueSeparation = par2_separation - par2.blobSize;
    # If the true separation is less than the par1 blob size, the contact was expected.
    if trueSeparation <= par1.blobSize:
        contactExpected += 1;
        if par2_separation in contactExpected_bySep.keys():
            contactExpected_bySep[par2_separation] += 1;
        else:
            contactExpected_bySep[par2_separation] = 1;
    else:
        not_contactExpected += 1;
        if par2_separation in not_contactExpected_bySep.keys():
            not_contactExpected_bySep[par2_separation] += 1;
        else:
            not_contactExpected_bySep[par2_separation] = 1;
    # Printing progress.
    print(f"Step {i+1}/10,000 Complete");
# Printing the results.
print(f"Proportion of Contacts That Were Expected: {contactExpected/(contactExpected + not_contactExpected)}");
print(f"Separation Status of the Expected Contacts: {contactExpected_bySep}");
print(f"Separation Status of the Unexpected Contacts: {not_contactExpected_bySep}");