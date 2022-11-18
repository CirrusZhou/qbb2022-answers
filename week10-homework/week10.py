#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

K562_model_predictions = [] #predictions
K562_observations = []
gene_names= []
descriptions = []

for i,line in enumerate(open(sys.argv[1])):
    if line.strip('"').startswith("##"):
        header = np.array(line.strip('"\r\n').split('\t'))
        K562_obs_idx = np.where(header=="E123")[0][0]
        print(K562_obs_idx)
        print(header) 
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        # if i < 10:
        #     print(fields)
        #     quit()
        K562_model_predictions.append(float(fields[4]))
        K562_observations.append(float(fields[K562_obs_idx]))
        gene_names.append(fields[1])
        descriptions.append(fields[2])

genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs = []

for geneoi in genesoi:
    genesoilocs.append(np.where(np.array(gene_names) == geneoi)[0][0])

for i in range(len(descriptions)):
    if "hemoglobin subunit" in descriptions[i]:
        genesoi.append(gene_names[i])
        genesoilocs.append(i)

fig, ax = plt.subplots()
ax.scatter(K562_model_predictions,K562_observations, color = "blue", s = 0.25, alpha = 1)
ax.set_xlabel("Predicted K562 expression level, \n10-fold cross-validated")
ax.set_ylabel("K562 expression level (log10)")

line_xs = np.linspace(min(max(K562_model_predictions),min(K562_observations)),min(max(K562_model_predictions),max(K562_observations)),100)
line_ys = 0+1*line_xs
ax.plot(line_xs, line_ys, color="maroon")

cor = pearsonr(K562_model_predictions,K562_observations)
ax.text(0.5, 3.75, "r^2 = " + str(round(cor.statistic**2,2) ) + '\nn = ' + str(len(K562_observations)))

for geneoi, idx in zip(genesoi, genesoilocs):
    ax.text(K562_model_predictions[idx],K562_observations[idx],geneoi, color = 'maroon', fontweight="demi")


ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.tight_layout()
plt.show()