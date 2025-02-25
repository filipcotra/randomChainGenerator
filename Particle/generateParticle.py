import random as rand;
import math;
import numpy as np;
import sys;

# Setting a constant for the distance between any two particles.
BOND_SIZE = 1.32;

# Purpose: To generate a particle with random coordinates that will
# have a Euclidean distance of 1.32 angstroms from the reference particle.
# Parameters:
#   refPar = The reference particle.
#   particleType = The init function for the particle to be generated.
# Return:
#   The randomly generated particle.
def generateParticle(refPar, particleType):
    rand.seed();
    X1 = refPar.xCoord;
    Y1 = refPar.yCoord;
    Z1 = refPar.zCoord;
    # Generate random spherical coordinates.
    theta = rand.uniform(0, math.pi);
    phi = rand.uniform(0, 2 * math.pi);
    # Convert spherical coordinates to Cartesian coordinates
    X2 = BOND_SIZE * math.sin(theta) * math.cos(phi) + X1;
    Y2 = BOND_SIZE * math.sin(theta) * math.sin(phi) + Y1;
    Z2 = BOND_SIZE * math.cos(theta) + Z1;
    # Returning new particle.
    return particleType(xCoord = X2, yCoord = Y2, zCoord = Z2);

# Setting a constant for the angle (in degrees) N, N+1, N+2.
ANGLE_DEGREES = 120;

# Purpose: To generate a particle N2 whose euclidean distance from
# particle N1, ensuring that the angle N, N1, N2 is 120 degrees.
# Parameters:
#   par_N = The particle N.
#   particleType = The init function for the particle to be generated.
# Return:
#   The randomly generated particle.
def generateParticle_N2(par_N, particleType):
    np.random.seed();
    par_N1 = par_N.next;
    # Convert coordinates for N and N1 to numpy arrays.
    N = np.array([par_N.xCoord, par_N.yCoord, par_N.zCoord]);
    N1 = np.array([par_N1.xCoord, par_N1.yCoord, par_N1.zCoord]);
    # Calculate the vector from N to N1.
    v_NN1 = N - N1;
    # Calculate the unit vector of v_NN1.
    v_NN1_unit = v_NN1 / np.linalg.norm(v_NN1);
    # Generate a random perpendicular vector.
    random_vector = np.random.randn(3);
    perp_vector = np.cross(v_NN1_unit, random_vector);
    # If the magnitude of the perpendicular vector is 0, it was
    # parallel or antiparallel to the original - set to 0, 0, 1
    # to ensure magnitude is not 0.
    if np.linalg.norm(perp_vector) == 0:
        perp_vector = np.array([0, 0, 1]);
    # Getting the unit vector of the perpendicular vector.
    perp_vector_unit = perp_vector / np.linalg.norm(perp_vector);
    # Generate a rotation axis which is orthogonal to both v_NN1 and perp_vector.
    rotation_axis = np.cross(v_NN1_unit, perp_vector_unit);
    rotation_axis_unit = rotation_axis / np.linalg.norm(rotation_axis);
    # Angle of 120 degrees in radians.
    angle = np.radians(ANGLE_DEGREES);
    # Rodrigues' rotation formula to find the rotated vector.
    v_NN2 = (v_NN1_unit * np.cos(angle) +
             np.cross(rotation_axis_unit, v_NN1_unit) * np.sin(angle) +
             rotation_axis_unit * np.dot(rotation_axis_unit, v_NN1_unit) * (1 - np.cos(angle)));
    # Scale the vector to the desired distance of 1.32.
    v_NN2 *= BOND_SIZE;
    # Calculate the coordinates of N2.
    N2 = N1 + v_NN2;
    # Double-checking the angle and distance. Closing if an issue is ever found,
    # as this would mean that the math is wrong.
    v_N1N2 = N2 - N1;
    dot_product = np.dot(v_NN1, v_N1N2);
    magnitude_a = np.linalg.norm(v_NN1);
    magnitude_b = np.linalg.norm(v_N1N2);
    angle_rad = np.arccos(dot_product / (magnitude_a * magnitude_b));
    angle_deg = np.degrees(angle_rad);
    if (not math.isclose(ANGLE_DEGREES, angle_deg, rel_tol = 0.1)
            or not math.isclose(BOND_SIZE, magnitude_a, rel_tol = 0.001)
            or not math.isclose(BOND_SIZE, magnitude_b, rel_tol = 0.001)):
        print(f"Things are going wrong: {angle_deg}, {magnitude_a}, {magnitude_b}");
        sys.exit(1);
    # Returning a particle with the appropriate coordinates for N2.
    N2_coords = N2.tolist();
    return particleType(xCoord = N2_coords[0], yCoord = N2_coords[1], zCoord = N2_coords[2]);
