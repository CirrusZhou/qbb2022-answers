import scanpy as sc
import matplotlib.pyplot as plt
import pandas as pd
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

#plot before filter
sc.tl.pca(adata)
sc.pl.pca(adata)


#plot after filter
sc.pp.recipe_zheng17(adata)
sc.tl.pca(adata)
sc.pl.pca(adata)


#cluster
sc.pp.neighbors(adata)
sc.tl.leiden(adata)

sc.tl.tsne(adata)
sc.pl.tsne(adata, color='leiden')

sc.tl.umap(adata,maxiter=1000)
sc.pl.umap(adata, color='leiden')


#distinguishing genes
#print(adata)
sc.tl.rank_genes_groups(adata,'leiden',method='t-test')
sc.pl.rank_genes_groups(adata)
sc.tl.rank_genes_groups(adata,'leiden',method='logreg')
sc.pl.rank_genes_groups(adata)



#get all gene_ids to see whether our markers are in them.
gene_id = []
for i in range(len(adata.var_names)):
    gene_id.append(adata.var_names[i])
    

#umap examples
sc.pl.umap(adata, color='Stmn1')
sc.pl.umap(adata, color='Tuba1a')
sc.pl.umap(adata, color='Ppia')

#violin examples
sc.pl.violin(adata, ['Aif1','Cx3cr1'], groupby='leiden' )
sc.pl.violin(adata, ['Ndnf','Trp73'], groupby='leiden' )
sc.pl.violin(adata, ['Higd1b','Mcam'], groupby='leiden' )

# create a dictionary to map cluster to annotation label
cluster2annotation = {
     '5': 'Astrocyte',
     '14': 'Astrocyte',
     '13': 'Astrocyte',
     '21': 'Astrocyte',
     '9': 'Oligodendrite',
     '10': 'Oligodendrite',
     '4': 'Oligodendrite',
     '6': 'Oligodendrite',
     '7': 'Oligodendrite',
     '13': 'Oligodendrite',
     '26': 'Microglia',
     '24': 'Endothelial cell',
     '25': 'Pericyte',
     '23': 'Pericyte',
     '0': 'Purkinje cell',
     '20': 'Purkinje cell',
     '16': 'Immune cell',
}

# add a new `.obs` column called `cell type` by mapping clusters to annotation using pandas `map` function
adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')
#plot the overall figure
sc.pl.umap(adata, color='cell type', legend_loc='on data',frameon=False, legend_fontsize=10, legend_fontoutline=2)