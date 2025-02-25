This code:
  1. Generates a random polypeptide chain made up of general particles representing amino-acids, according to the following constraints:
    a. The euclidean distance between consecutive particles is 1.32 angstroms
    b. The bond angle N/N+1/N+2 is 120 degrees
  2. Simulates a folding path by populating contacts in the random chain (defined by euclidean distance < 6 angstroms) and randomly defining their order of incidence
  3. Builds a distribution to define the number of assumed folding steps corresponding to "blob-based" particle separations

To run the code, simply download the directory, navigate within it, and enter the following into the terminal: python randomChainGenerator.py
