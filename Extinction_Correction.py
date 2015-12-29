'''
Author: Devin Whitten
Institution: University of Notre Dame
Date: 11/6/2015

Here I am just applying the extinction corrections given from the following papers,
one set is particular to GALEX, and the other to the SDSS filers.

SDSS -
http://arxiv.org/pdf/astro-ph/0612034v1.pdf

GALEX -
http://dolomiti.pha.jhu.edu/papers/Bianchi_GALEX_SF.pdf

These stars are high in galactic latitude, so we should expect a lot correction to be necessary.

'''
'''
NU,   NU_err,   FU,   FU_err,   U_SDSS,   U_SDSS_err,   G_SDSS,   G_SDSS_err,   R_SDSS,   R_SDSS_err,   I_SDSS,   I_SDSS_err,   Z_SDSS,   Z_SDSS_err,     E_bv
'''

def Correction(line):
    stringline = line.strip().split(',')
    newline = []
    for element in stringline:
        newline.append(float(element))
    # Grab U, G, R, I, Z, FU, NU, Ebv

    # GALEX CORRECTION coefficients

    E_bv = newline[14]

    NU0 = newline[0] - E_bv * 7.95
    FU0 = newline[2] - E_bv * 8.06
    U0 = newline[4] - E_bv * 5.2
    G0 = newline[6] - E_bv * 3.2
    R0 = newline[8] - E_bv * 2.8
    I0 = newline[10] - E_bv * 2.1
    Z0 = newline[12] - E_bv * 1.5


    # Return Order ->  FU, FU0, NU, NU0, U, U0, G, G0, R, R0, I, I0, Z, Z0,

    return newline[0], NU0, newline[2], FU0, newline[4], U0, newline[6], G0, newline[8], R0, newline[10], I0, newline[12], Z0

fh = open("Pristine_2arc_Update.csv")
Line = fh.readline().split(',')
print Line

count = 0

NU = []
NU0 = []

FU = []
FU0 = []

U = []
U0 = []

G = []
G0 = []

R = []
R0 = []

I = []
I0 = []

Z = []
Z0 = []


for line in fh:
    outarray = Correction(line)
    if (len(NU) == 0):
        print len(outarray)

    NU.append(outarray[0])
    NU0.append(outarray[1])

    FU.append(outarray[2])
    FU0.append(outarray[3])

    U.append(outarray[4])
    U0.append(outarray[5])

    G.append(outarray[6])
    G0.append(outarray[7])

    R.append(outarray[8])
    R0.append(outarray[9])

    I.append(outarray[10])
    I0.append(outarray[11])

    Z.append(outarray[12])
    Z0.append(outarray[13])


print "Writing to Pristine_2arc_Corrected.csv"
print "Number of Stars:  " + str(len(U))
fout = open("Pristine_2arc_Corrected.csv", 'w')
fout.write("NU,   NU0,   FU,   FU0,   U,   U0,   G,   G0,   R,   R0,   I,   I0,   Z,   Z0" + "\n")

for i in range(len(U)):
    fout.write(str(NU[i]) + "," + str(NU0[i]) + "," +
    str(FU[i]) + "," + str(FU0[i]) + "," +
    str(U[i]) + "," + str(U0[i]) + "," +
    str(G[i]) + "," + str(G0[i]) + "," +
    str(R[i]) + "," + str(R0[i]) + "," +
    str(I[i]) + "," + str(I0[i]) + "," +
    str(Z[i]) + "," + str(Z0[i]) + "\n")

fout.close()
