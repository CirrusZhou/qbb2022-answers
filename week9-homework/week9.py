import numpy as np
import scipy 
from matplotlib import pyplot as plt
import seaborn 

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
print(input_arr[:4])


col_names = list(input_arr.dtype.names)[1:]#get all names of sample
print(col_names)

row_names = [] # get all gene id
for i in input_arr:
    row_names.append(i[0])
row_names_arr = np.asarray(row_names)
#print(row_names[:5])

input_subls=[] # get rid of gene id, only have numbers
for i in input_arr:
    i=list(i)[1:]
    input_subls.append(i)
#print(input_subls[:5])

input_subarr=np.asarray(input_subls)
input_median = np.median(input_subarr,axis=1) # calculate median for each 
print(input_median[:5])

location = np.where(input_median != 0)
#print(location)
#print(input_median[location])
#print(row_names_arr[location])
row_names_arr = row_names_arr[location] #get new gene id list, remove those median == 0
input_subarr = input_subarr[location]#get new input array, remove those median == 0
print(np.shape(input_subarr))
ones = np.ones(np.shape(input_subarr))
#print(ones/10)
input_subarr_trans = np.log2(input_subarr + ones/10) # transform FPKM to log2


linkage = scipy.cluster.hierarchy.linkage(input_subarr_trans,'ward')
print(linkage)

scipy.cluster.hierarchy.leaves_list(linkage)

fig = plt.figure()
seaborn.clustermap(input_subarr_trans,method = "ward", z_score=0 )
#z_score = 0 means get relative value between samples
plt.savefig("heatmap_sample1.png")
plt.close()

scipy.cluster.hierarchy.dendrogram(linkage)
plt.savefig("dendrogram_gene.png")
plt.close()







