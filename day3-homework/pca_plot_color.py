#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

coordinate = np.genfromtxt("PCA_pop_gender", 
                                dtype = None,
                                encoding = None,
                                names = ["sample","pop","super_pop","gender","0","PCA1","PCA2","PCA3"])# let it guess the data type

#print(coordinate[0][1])

# the coordinate looks like:
# ('HG01880', 'ACB', 'AFR', 'female', 0, 0.0116396, -0.00313458, -0.0162419)

scatter_x = coordinate["PCA1"]
scatter_y = coordinate["PCA2"]
pop = coordinate["pop"]
super_pop = coordinate["super_pop"]
gender = coordinate["gender"]

#print(set(pop))

#create color dictionaries for different label
#first we need to create a color list!
'''
import random
color_list=[]
for i in range(30):
    a = tuple([random.random() for k in range(3)])
    color_list.append(a)
    color_list=list(set(color_list))
#color dictionary for pop
pop_dict={}
for k, i in enumerate(set(pop)):
    pop_dict[i] = color_list[k]

#color dictionary for super_pop
super_pop_dict={}
for k, i in enumerate(set(super_pop)):
    super_pop_dict[i] = color_list[k]
    
#color dictionary for super_pop
gender_dict={}
for k, i in enumerate(set(gender)):
    gender_dict[i] = color_list[k]
#print(pop_dict)


# create the color list
pop_ls=[]
super_pop_ls=[]
gender_ls=[]
for i in range(len(coordinate)):
    pop_ls.append(pop_dict[pop[i]])
    super_pop_ls.append(super_pop_dict[super_pop[i]])
    gender_ls.append(gender_dict[gender[i]])
#print(pop_ls)

'''

# reference: to get proper legend, refer to the link below
# https://stackoverflow.com/questions/47006268/matplotlib-scatter-plot-with-color-label-and-legend-specified-by-c-option

fig, ax = plt.subplots()
for g in np.unique(pop):
    ix = np.where(pop == g)
    ax.scatter(scatter_x[ix], scatter_y[ix], label = g, s = 10)
    #ax.scatter(scatter_x[ix], scatter_y[ix], c = pop_dict[g], label = g, s = 10)
# put the legend aside to avoid covering plot
ax.legend(bbox_to_anchor=(1,1))
#plt.show()
# give the plot a good size to show everything we plot, include the legend
fig.set_size_inches(10, 8)
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.title.set_text('PCA of individuals with different populations according to genotypes(SNPs)')
#plt.show()
plt.savefig("ex3_a.png")
plt.close(fig)



fig, ax = plt.subplots()
for g in np.unique(super_pop):
    #find the index of all g in our data
    ix = np.where(super_pop == g)
    ax.scatter(scatter_x[ix], scatter_y[ix], label = g, s = 10)
    #ax.scatter(scatter_x[ix], scatter_y[ix], c = super_pop_dict[g], label = g, s = 10)
# put the legend aside to avoid covering plot
ax.legend(bbox_to_anchor=(1,1))
#plt.show()
# give the plot a good size to show everything we plot, include the legend
fig.set_size_inches(10, 8)
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.title.set_text('PCA of individuals with different superpopulations according to genotypes(SNPs)')
plt.savefig("ex3_b.png")
plt.close(fig)


fig, ax = plt.subplots()
for g in np.unique(gender):
    ix = np.where(gender == g)
    ax.scatter(scatter_x[ix], scatter_y[ix], label = g, s = 10)
    #ax.scatter(scatter_x[ix], scatter_y[ix], c = gender_dict[g], label = g, s = 10)
# put the legend aside to avoid covering plot
ax.legend(bbox_to_anchor=(1,1))
#plt.show()
# give the plot a good size to show everything we plot, include the legend
fig.set_size_inches(10, 8)
ax.set_ylabel("PCA2")
ax.set_xlabel("PCA1")
ax.title.set_text('PCA of individuals with different gender according to genotypes(SNPs)')

plt.savefig("ex3_c.png")
plt.close(fig)






