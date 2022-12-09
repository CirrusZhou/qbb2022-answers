#stimulation

import numpy
import matplotlib.pyplot as plt
import math
import seaborn as sns

#we have 1000 people, 2000 alleles,
n=100*2
p=0.5

x_axis = [0]
generation_ls=[]# the list to store generation to fix frequency
generation=0

'''
for i in range(10000):
    generation+=1
    s = numpy.random.binomial(n,p)
    p=s/n
    frequency.append(p)
    x_axis.append(generation)
    if 1 in frequency:
        generation_ls.append(generation)
        break
    if 0 in frequency:
        generation_ls.append(generation)
        break


plt.plot(x_axis, frequency)
plt.xlabel("Generation")
plt.ylabel("Frequency")
plt.text(0,0.3,"0.3")
plt.show()

'''
'''
for j in range(1000):
    generation=0
    p=0.5
    for i in range(10000):
        generation+=1
        s = numpy.random.binomial(n,p)
        p=s/n
        x_axis.append(generation)
        if p==0:
            generation_ls.append(generation)
            break
        if p==1:
            generation_ls.append(generation)
            break
            
print(generation_ls)
plt.hist(generation_ls,bins=50,density=True)   

plt.xlabel("Generation")
plt.ylabel("Density")  

plt.show()
'''

# pop_size = [100,1000,10000,100000,1000000,10000000]
# x_axis = []
# generation_ls = []

# for j in pop_size:
#     x_axis.append(math.log(j))
#     p=0.5
#     generation=0
#     print(j,p)
#     for i in range(10000000000):
#         generation+=1
#         s = numpy.random.binomial(2*j,p)
#         p=s/(2*j)
#         #print(p)
#         if p==0:
#             generation_ls.append(math.log(generation))
#             break
#         if p==1:
#             generation_ls.append(math.log(generation))
#             break




# plt.plot(x_axis,generation_ls)
# plt.xlabel("log(Population size)")
# plt.ylabel("log(Generations)")
# plt.show()
#



import pandas as pd
df=pd.DataFrame(columns = ['generation','allele_freq'])
print(df)

allele_freq = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99]
n=1000
generation_ls=[]
for i in allele_freq:
    generation_ls_ls=[]
    for j in range(100):
        p=i
        generation=0
        for k in range(1000000):
            generation+=1
            s = numpy.random.binomial(2*n,p)
            p=s/(2*n)
            if p==0:
                row=[generation,i]
                break
            if p==1:
                row=[generation,i]
                break
        df.loc[len(df.index)]=row


sns.violinplot(x='allele_freq',y='generation',data=df)
plt.title("population size is 1000")
plt.xlabel("Allele frequency")
plt.ylabel("Generations")
plt.show()

