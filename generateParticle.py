import random as rand;
import math;
import numpy as np;
import sys;

BOND_SIZE = 1.32;

# Given a particle type, this will randomly generate a particle
# with random coordinates that have an exact Euclidean distance
# of 1.32 angstroms from the current particle.
def generateParticle(currPar, particleType):
    rand.seed();
    X1 = currPar.xCoord;
    Y1 = currPar.yCoord;
    Z1 = currPar.zCoord;
    # Generate random spherical coordinates.
    theta = rand.uniform(0, math.pi);
    phi = rand.uniform(0, 2 * math.pi);
    # Convert spherical coordinates to Cartesian coordinates
    X2 = BOND_SIZE * math.sin(theta) * math.cos(phi) + X1;
    Y2 = BOND_SIZE * math.sin(theta) * math.sin(phi) + Y1;
    Z2 = BOND_SIZE * math.cos(theta) + Z1;
    # Returning new particle.
    return particleType(xCoord = X2, yCoord = Y2, zCoord = Z2);

ANGLE_DEGREES = 120;

# Trying this out.
def generateParticle_N2(currPar, particleType):
    np.random.seed();
    # Convert coordinates to numpy arrays.
    N = np.array([currPar.xCoord, currPar.yCoord, currPar.zCoord]);
    N1 = np.array([currPar.next.xCoord, currPar.next.yCoord, currPar.next.zCoord]);
    # Calculate the vector from N to N1.
    v_NN1 = N1 - N;
    # Calculate the unit vector of v_NN1.
    v_NN1_unit = v_NN1 / np.linalg.norm(v_NN1);
    # Generate a random perpendicular vector.
    random_vector = np.random.randn(3);
    perp_vector = np.cross(v_NN1_unit, random_vector);
    if np.linalg.norm(perp_vector) == 0:
        perp_vector = np.array([0, 0, 1]);
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
    v_NN2 *= 1.32;
    # Calculate the coordinates of N2.
    N2 = N1 + v_NN2;
    # Double-checking the angle and distance.
    v_N1N2 = N2 - N1;
    dot_product = np.dot(v_NN1, v_N1N2);
    magnitude_a = np.linalg.norm(v_NN1);
    magnitude_b = np.linalg.norm(v_N1N2);
    angle_rad = np.arccos(dot_product / (magnitude_a * magnitude_b));
    angle_deg = np.degrees(angle_rad);
    if (not math.isclose(120, angle_deg, rel_tol = 0.1)
            or not math.isclose(1.32, magnitude_a, rel_tol = 0.001)
            or not math.isclose(1.32, magnitude_b, rel_tol = 0.001)):
        print(f"Things are going wrong: {angle_deg}, {magnitude_a}, {magnitude_b}");
        sys.exit(1);

    N2_coords = N2.tolist();
    return particleType(xCoord = N2_coords[0], yCoord = N2_coords[1], zCoord = N2_coords[2]);
