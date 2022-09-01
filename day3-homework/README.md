# QBB2022 - Day 3 - Homework Exercises Submission


##Exercise 1
1. (reference :https://www.jianshu.com/p/fa6790e68818)
	use this command in bash to turn vcf file into plink file:
	plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz  --recode --out testacc --const-fid --allow-extra-chr
	
2. use this command to get bed (binary) file from ped file:
	plink --allow-extra-chr --file testacc --noweb --make-bed --out testacc

3. use this command to carry out PCR analysis:
	plink --allow-extra-chr --threads 20 -bfile testacc --pca 20 --out testacc
	
4. finally we get two important files:
	.eigenval tells us how a PCA weighs, it looks like:
	(base) [~/qbb2022-answers/day3-homework $]head testacc.eigenval
	48.2938
	13.8526
	5.92139
	4.46397
	4.03391
	3.19185
	3.1101
	2.81778
	2.78896
	2.71115
	
	.eigenvec tells us the eigenvector, it looks like:
	(base) [~/qbb2022-answers/day3-homework $]head testacc.eigenvec
	0 HG00096 -0.0109316 -0.0249319 0.00534958 -0.0229322 0.00153724 -0.00108572 -0.00203851 -0.0018136 -0.00119036 0.00044587 3.42172e-05 0.00259313 0.00118551 0.003987 -0.00192979 -0.00323212 0.000480119 0.00356345 -0.0030182 -0.00268067
	0 HG00097 -0.0121359 -0.0290234 0.0192942 -0.0190357 -0.000235588 -6.04413e-05 0.000190254 0.000163091 -0.00238475 -0.00170071 -0.00124102 0.00310081 -0.000765667 0.000310604 0.00246669 0.000621177 0.000752262 -8.12568e-05 0.00185132 0.00251386
	0 HG00099 -0.0127633 -0.0249592 0.00975894 -0.0240232 0.00274482 -0.000739866 0.00113016 0.00156371 0.00189958 0.000621918 -1.16209e-05 0.00335381 -0.00155806 0.00218421 -0.000504419 0.000656 -3.49474e-05 0.00126158 -0.00211097 0.000657391

##Exercise 2	
1. let's see what is in the .eigenvec 
	
	.eigenvec, .eigenvec.var (principal components)
	Produced by --pca. Accompanied by an .eigenval file, which contains one eigenvalue per line.

	The .eigenvec file is, by default, a space-delimited text file with no header line and 2+V columns per sample, where V is the number of requested principal components. The --pca 'header' modifier causes a header line to be written, and the 'tabs' modifier makes this file tab-delimited. The first two columns are the sample's FID/IID, and the rest are principal component weights in the same order as the .eigenval values (if the header line is present, these columns are titled 'PC1', 'PC2', ...).

	With the 'var-wts' modifier, an .eigenvec.var file is also generated. It replaces the FID/IID columns with 'CHR', 'VAR', 'A1', and 'A2' columns containing chromosome codes, variant IDs, A1 alleles, and A2 alleles, respectively; otherwise the formats are identical.
	
2.  try do get the first three PCA coordinators in .eigenvec
	cut -d " " -f 2,3,4 testacc.eigenvec > three_PCA
	
	then run the pca_plot.py, we get two plots!
	
3.  Two plots all look like triangle😂, and more dots on the vertexes. 
	the structure represents different subgroups, and also the relationship between those subgroups.
	
## Exercise 3
1. let's see how the metadata looks like:
	sample	pop	super_pop	gender
	HG00096	GBR	EUR	male
	HG00097	GBR	EUR	female
	HG00098	GBR	EUR	male
	
2. then how the .eigenvec looks like:
	0 HG00096 -0.0109316 -0.0249319 0.00534958 -0.0229322 0.00153724 -0.00108572 -0.00203851 -0.0018136 -0.00119036 0.00044587 3.42172e-05 0.00259313 0.00118551 0.003987 -0.00192979 -0.00323212 0.000480119 0.00356345 -0.0030182 -0.00268067
	0 HG00097 -0.0121359 -0.0290234 0.0192942 -0.0190357 -0.000235588 -6.04413e-05 0.000190254 0.000163091 -0.00238475 -0.00170071 -0.00124102 0.00310081 -0.000765667 0.000310604 0.00246669 0.000621177 0.000752262 -8.12568e-05 0.00185132 0.00251386
	0 HG00099 -0.0127633 -0.0249592 0.00975894 -0.0240232 0.00274482 -0.000739866 0.00113016 0.00156371 0.00189958 0.000621918 -1.16209e-05 0.00335381 -0.00155806 0.00218421 -0.000504419 0.000656 -3.49474e-05 0.00126158 -0.00211097 0.000657391
	
3. reference for "join" in unix:
	https://shapeshed.com/unix-join/#what-is-the-join-command-in-unix
	
	join -1 1 -2 2 <(sort -k 1 integrated_call_samples.panel) <(sort -k 2 testacc.eigenvec)  > joined_file
	
	cut -d " " -f 1-8 joined_file > PCA_pop_gender
	
4. see how many pops and super_pops
	cut -d " " -f 2 PCA_pop_gender | sort|uniq -c
	  97 ACB
	  61 ASW
	  86 BEB
	 100 CDX
	  99 CEU
	 106 CHB
	 105 CHS
	  95 CLM
	 100 ESN
	 105 FIN
	 100 GBR
	 106 GIH
	 113 GWD
	 107 IBS
	 102 ITU
	 105 JPT
	  99 KHV
	 103 LWK
	  90 MSL
	  64 MXL
	  85 PEL
	  96 PJL
	 104 PUR
	 102 STU
	 111 TSI
	 107 YRI
	

	cut -d " " -f 3 PCA_pop_gender | sort|uniq -c
	 671 AFR
	 348 AMR
	 515 EAS
	 522 EUR
	 492 SAS
	

