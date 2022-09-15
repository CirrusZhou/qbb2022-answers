# How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? 

import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy import stats

genome_len = 1000000 # the genome has 1000000 bps
coverage = 5
frag_len = 100

reads_num = int(genome_len * coverage / frag_len) # calculate how many reads we need to get 5* coverage. we need to turn it into int then.

# create a one dimension array with 1000000 zeros.

arr = np.zeros(genome_len)# initiate an array to store the counts for all 1000000 bps. Zero for all at the beginning.

for i in range (reads_num): # we do the rain drop for certain times
    position = random.randint(0, genome_len-frag_len-1)# get the random position the rain drop on
    for k in range(frag_len): # we need to add 1 to this position in our arr and also to 99 positions after it.
        arr[position+k]+=1

# count how many 0 in the array
num_0 = list(arr).count(0)
print("0 coverage bp in simulation: ", num_0)# to see the bp number with 0 coverage in our simulation model
print("0 coverage bp in poisson distribution: ", stats.poisson.pmf(0,coverage)*len(arr))

fig, ax = plt.subplots()
ax.hist(arr, bins=list(range(40)))
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))# to make locator integer instead of float
    
# plot the poisson distribution (reference:https://www.jianshu.com/p/2ed40d7a559a)
sample_poisson = np.random.poisson(coverage, size=genome_len)
freq = {}
for i in sample_poisson:
    if i not in freq:
        freq[i]=0
    freq[i]+=1
arr_poi=list(freq.keys())
arr_poi.sort()
x_data=np.array(arr_poi)
y_data=np.array([freq[i] for i in x_data])
plt.plot(x_data,y_data)
#plt.savefig("exercise1_4.png")