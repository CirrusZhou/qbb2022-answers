
import matplotlib.pyplot as plt
import numpy as np
from vcfParser import parse_vcf


vcf=parse_vcf('snp_freebayes.vcf')

#DP:read depth
#GQ:Genotype Quality, the Phred-scaled marginal (or unconditional) probability, the Phred-scaled marginal (or unconditional) probability of the called genotype
#AF:Estimated allele frequency in the range (0,1]

effect_name={}# to store all possible effects

# effect_list=vcf[1][7]['ANN'].split(',')
# for i in effect_list:
#     each=i.split("|")
#     if each[1] not in effect_name.keys():
#         effect_name[each[1]]=0
#     else:
#         effect_name[each[1]]+=1




read_depth=[]
quality=[]
frequency=[]
for n,line in enumerate(vcf):
    if n == 0:
        continue
    #get all the frequency
    try:
        frequency.append(float(line[7]['AF']))
    except:
        continue
    #get all the effect
    effect_list=line[7]['ANN'].split(',')
    for i in effect_list:
        each=i.split("|")
        if each[1] not in effect_name.keys():
            effect_name[each[1]]=1
        else:
            effect_name[each[1]]+=1
    
    #get all the read depth and quality
    for i in range(9,19):
        try:
            read_depth.append(int(line[i][2]))
        except:
            continue
        try:
            quality.append(float(line[i][1]))
        except:
            continue


fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(48,24),squeeze=False)
ax[0][0].hist(read_depth)
ax[0][0].set_yscale("log")
ax[0][0].set_ylabel("Counts")
ax[0][0].set_xlabel("Read depths")
ax[0][0].title.set_text("Distribution of varient genotypes' read depth")

ax[1][0].hist(quality)
ax[1][0].set_ylabel("Counts")
ax[1][0].set_xlabel("Quality")
ax[1][0].title.set_text("Distribution of variant genotypes' quality")
ax[1][0].set_yscale("log")

ax[0][1].hist(frequency)
ax[0][1].set_ylabel("Counts")
ax[0][1].set_xlabel("Frequency")
ax[0][1].title.set_text("Distribution of variants' frequency")


effect_name_keys=[]
effect_name_values=[]

for i in effect_name.keys():
    effect_name_keys.append(i)
    effect_name_values.append(effect_name[i])

x=np.array(effect_name_keys)
y=np.array(effect_name_values)
ax[1][1].bar(x,y)
plt.xticks(fontsize=8,rotation=-30)
ax[1][1].set_ylabel("Counts")
ax[1][1].set_xlabel("Predicted effects")
ax[1][1].title.set_text("Summary of predicted effects")
ax[1][1].set_yscale("log")

fig.savefig("week3_plot.png")
