#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1] 
fs = open( vcf )#put in vcf file we need to plot

ac = []#create a list to store all the allele count
for i, line in enumerate( fs ):# for each line in the vcf file
    if "#" in line:
        continue # skip all header lines 
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
# density: each bin will display the bin's raw count divided by the total number of counts and the bin width
ax.hist( ac, density=True )
# for log scale y axis, refer to : https://stackoverflow.com/questions/47850202/plotting-a-histogram-on-a-log-scale-with-matplotlib
plt.yscale("log") 
plt.ylim((0.000001, 0.005))#we can not start from 0 because log(0) does not exist

ax.set_ylabel("density")
ax.set_xlabel("allele count")
ax.title.set_text(f"density of different allele count ({vcf})")
fig.savefig( vcf + ".png" )
fs.close()

