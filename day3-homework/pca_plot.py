#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

coordinate = np.genfromtxt("three_PCA", 
                                dtype = None,
                                encoding = None,
                                names = ["sample","PCA1","PCA2","PCA3"])# let it guess the data type

# the coordinate looks like:
#('HG00097', -0.0121359, -0.0290234, 0.0192942)
#print (type(coordinate))

fig, ax = plt.subplots()

ax.scatter(coordinate["PCA1"], coordinate["PCA2"])
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")

#plt.show()

plt.savefig("ex2_a.png")
plt.close(fig)

fig2, ax2 = plt.subplots()
ax2.scatter(coordinate["PCA1"], coordinate["PCA3"])
ax2.set_ylabel("PCA3")
ax2.set_xlabel("PCA1")

#plt.show()

plt.savefig("ex2_b.png")
plt.close(fig2)
