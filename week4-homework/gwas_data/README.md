```
1.convert vcf file to plink file
vcftools --vcf reorg_genotypes.vcf --plink --out reorg_genotypes

2.convert file into binary
plink --file reorg_genotypes --make-bed --out reorg_genotypes

3.pca analysis
plink --threads 20 -bfile reorg_genotypes --pca 10 --out reorg_genotypes

4.calculate allele frequency
plink --noweb --bfile reorg_genotypes --freq --out reorg_allele_frequency

5.quantative association testing for each genotype
plink --vcf reorg_genotypes.vcf --linear --pheno CB1908_IC50.txt --covar reorg_genotypes.eigenvec --allow-no-sex --out reorg_phenotype_gwas
plink --vcf reorg_genotypes.vcf --linear --pheno GS451_IC50.txt --covar reorg_genotypes.eigenvec --allow-no-sex --out GS451_reorg_phenotype_gwas

6.the most significant SNP
CB1908:
rs10876043 11.086239113587677
poteintial assocaited genes include:LIMA1, LARP4, DIP2B, ATF1


GS451:
rs7257475 6.844663962534939
poteintial assocaited genes include:ZNF486, ZNF826, ZNF737,ZNF626
```