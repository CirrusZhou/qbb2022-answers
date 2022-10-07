
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns






# file1=open('reorg_genotypes.eigenvec')
#
# pca1=[]
# pca2=[]
# for line in file1:
#     eachline = line.split(" ")
#     pca1.append(float(eachline[2]))
#     pca2.append(float(eachline[3]))
#
# # print(pca1[:3])
# # print(pca2[:3])
#
# x=np.array(pca1)
# y=np.array(pca2)
#
# fig, ax = plt.subplots()
# ax.scatter(x,y,s=10)
# ax.set_xlabel('PCA1')
# ax.set_ylabel('PCA2')
# ax.title.set_text('Genometype PCA1-PCA2')
# plt.savefig("reorg_pca1-pca2")








# allele_freq=[]
# file2=open('allele_frequency.frq')
# for n,line in enumerate(file2):
#     if n==0:
#         continue
#     eachline=line.strip()
#     eachline=eachline.split()
#     allele_freq.append(float(eachline[4]))
#
# fig, ax = plt.subplots()
# ax.hist(allele_freq,bins=50)
# ax.set_ylabel("Count")
# ax.set_xlabel("Allele frequency")
# ax.title.set_text(f"Distribution of allele frequency")
# plt.savefig("AF.png")








##
# file3=open('genotypes.vcf')
# reorg_ls=[]
# new_file=''
# for line in file3:
#     if line.startswith("#CHROM"):
#         target=line.split("\t")
#         for i in target:
#             if '_' in i:
#                 i=i[5:]
#             reorg_ls.append(i)
#             reorg_str="\t".join(reorg_ls)
#         new_file+=reorg_str
#     else:
#         new_file+=line
# txt=open("reorg_genotypes.vcf","w").write(new_file)










file4=open('GS451_reorg_phenotype_gwas.assoc.linear')
file4_dict={}
for i,line in enumerate(file4):
    if i==0:
        line.strip()
        col_name=line.split()
        file4_dict[col_name[0]]=[]
        file4_dict[col_name[8]]=[]
        file4_dict['SNP']=[]
        #print(file4_dict)
        continue
    line.strip()
    line_ls=line.split()
    if line_ls[4]=="ADD":
        file4_dict[col_name[0]].append(int(line_ls[0]))
        file4_dict[col_name[8]].append(float(line_ls[8]))
        file4_dict['SNP'].append(line_ls[1])
gwas_sumstats = pd.DataFrame(file4_dict)
   
#reference: https://gwaslab.com/2021/03/28/mahattan-plot/     
gwas_sumstats["i"]=gwas_sumstats.index
gwas_sumstats["LOG10_P"]=-np.log10(gwas_sumstats["P"])
special_p=[]
special_x=[]

for i,element in enumerate(gwas_sumstats["LOG10_P"]):
    if element >= -np.log10(1e-5):
        special_p.append(element)
        special_x.append(gwas_sumstats["i"][i])








# plot = sns.relplot(data=gwas_sumstats, x='i', y='LOG10_P',aspect=2.3,
#                    hue='CHR', palette = 'dark', s=4, legend=None)
# chrom_df=gwas_sumstats.groupby('CHR')['i'].median()
# plot.ax.set_xticks(chrom_df)
# plot.ax.set_xticklabels(chrom_df.index)
# plot.ax.set_xlabel('CHR')
# plot.ax.set_ylim(0,20)
# plot.ax.axhline(y=-np.log10(1e-5), linewidth = 2,linestyle="--",color="grey")
# plot.fig.suptitle('Association between SNP and CB1908 IC50')
#
# plot2 = plt.scatter(special_x,special_p,c='r',s=5)
#
# plt.savefig("manhattan_CB1908.png")










# find the most significant SNP
location=list(gwas_sumstats["LOG10_P"]).index(max(gwas_sumstats["LOG10_P"]))
SNP_name=gwas_sumstats['SNP'][location]
SNP_log10P = gwas_sumstats["LOG10_P"][location]
print(location,gwas_sumstats['SNP'][location],gwas_sumstats["LOG10_P"][location])
#184404 rs10876043 11.086239113587677
#12	49190411	rs10876043	A	G	.	.
#240915 rs7257475 6.844663962534939

file5=open('reorg_genotypes.vcf')
for i,line in enumerate(file5):
    if line.startswith("#"):
        continue
    if SNP_name in line:
        line.strip()
        line_ls=line.split()
        genotype=line_ls[9:]


file6=open('GS451_IC50.txt')
phenotype=[]
for i,line in enumerate(file6):
    if i ==0:
        continue
    line.strip()
    line_ls=line.split()
    phenotype.append(line_ls[2])
    
dict_box={}
dict_box["A/A"]=[]
dict_box["A/G"]=[]
dict_box["G/G"]=[]

for i,element in enumerate(genotype):
    if element=="0/0":
        try:
            dict_box["A/A"].append(float(phenotype[i]))
        except:
            print("NA for A/A")
    if element=="0/1" or element=="1/0":
        try:
            dict_box["A/G"].append(float(phenotype[i]))
        except:
            print("NA for A/G")
    if element=="1/1":
        try:
            dict_box["G/G"].append(float(phenotype[i]))  
        except:
            print("NA for G/G") 

#print(dict_box["A/A"])

labels=["0/0","0/1","1/1"]
#[dict_box["A/A"],dict_box["A/G"],dict_box["G/G"]]
plt.boxplot((dict_box["A/A"],dict_box["A/G"],dict_box["G/G"]),labels=labels)
plt.xlabel("Genotype")
plt.ylabel("GS451 IC50")
plt.savefig("GS451_boxplot_rs10876043.png")









