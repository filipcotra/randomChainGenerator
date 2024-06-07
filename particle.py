import math;

# Class to represent the particles that will be randomly placed.
# Attributes will just be coordinates.
class particle:
    def __init__(self, xCoord, yCoord, zCoord):
        self.xCoord = xCoord;
        self.yCoord = yCoord;
        self.zCoord = zCoord;
        self.next = None;
        self.contactSet = set();

    def setNext(self, nextPar):
        self.next = nextPar;

    def addContact(self, contactPar):
        self.contactSet.add(contactPar);

    def getContacts(self):
        return self.contactSet;

# Glycine
class G_particle(particle):
    N_SCR = 0.45;
    fb_SCS = 2.16;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Proline
class P_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.14;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Alanine
class A_particle(particle):
    N_SCR = 0.89;
    fb_SCS = 1.46;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Valine
class V_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.14;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Leucine
class L_particle(particle):
    N_SCR = 1.78;
    fb_SCS = 1.06;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Isoleucine
class I_particle(particle):
    N_SCR = 1.76;
    fb_SCS = 1.06;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Methionine
class M_particle(particle):
    N_SCR = 2.23;
    fb_SCS = 1.06;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Cysteine
class C_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.26;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Phenylalanine
class F_particle(particle):
    N_SCR = 2.68;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Tyrosine
class Y_particle(particle):
    N_SCR = 3.12;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Tryptophan
class W_particle(particle):
    N_SCR = 3.12;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Histidine
class H_particle(particle):
    N_SCR = 2.23;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Lysine
class K_particle(particle):
    N_SCR = 2.68;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Arginine
class R_particle(particle):
    N_SCR = 3.12;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Glutamine
class Q_particle(particle):
    N_SCR = 2.23;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Asparagine
class N_particle(particle):
    N_SCR = 1.78;
    fb_SCS = 1.06;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Glutamic acid
class E_particle(particle):
    N_SCR = 1.78;
    fb_SCS = 1;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Aspartic acid
class D_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.06;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Serine
class S_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.26;
    blobSize = math.ceil(N_SCR * fb_SCS);

# Threonine
class T_particle(particle):
    N_SCR = 1.34;
    fb_SCS = 1.14;
    blobSize = math.ceil(N_SCR * fb_SCS);
