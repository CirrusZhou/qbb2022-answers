#

## exercise 1
###1. 
	--- Subsetting exons.chr21.bed.vcf
	    + Covering 1107407 bp
	--- Subsetting processed_pseudogene.chr21.bed.vcf
	    + Covering 956640 bp
	--- Subsetting protein_coding.chr21.bed.vcf
	    + Covering 13780687 bp

###2. 
1. method 1: open the file and see whether they are the same.
2. method 2: use conda to install imagemagick
	reference:https://askubuntu.com/questions/209517/does-diff-exist-for-images
	'conda install -c conda-forge imagemagick'
	store the difference in the *difference.png
	'compare -compose src exons.chr21.bed.vcf.png /Users/cmdb/cmdb-plot-vcfs/cache/exons.chr21.bed.vcf.png	 exon_difference.png'
	'compare -compose src processed_pseudogene.chr21.bed.vcf.png /Users/cmdb/cmdb-plot-vcfs/cache/processed_pseudogene.chr21.bed.vcf.png	 processed_pseudogene_difference.png'
	'compare -compose src protein_coding.chr21.bed.vcf.png /Users/cmdb/cmdb-plot-vcfs/cache/protein_coding.chr21.bed.vcf.png	 protein_coding_difference.png'

###3
1. lncRNA: because they are long, and are not trancribed. they function as RNA by interact with DNA, RNA or proteins.
2. rRNA: represent ribosomal RNA. combine proteins to make ribosome.
3. miRNA: small non-coding RNA which regulate the transcriptome.
4. TEC: to be experimentally comfirmed. This is very interesting because nobody has studied them!  

##exercise 2
1. use the following code to give the proper y scale, axis title and the plot title
	'
	plt.yscale("log")
	ax.set_ylabel("density")
	ax.set_xlabel("allele count")
	ax.title.set_text("density of different allele count")
	'
	but I do not know how to set the same y axis

2. modify the subset_regions.sh
	from:
	'
	for TYPE in protein_coding processed_pseudogene
	do
	    echo "--- Creating $TYPE.$CHR.bed"
	    grep $TYPE $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="gene"){print $1, $4-1, $5}}' > $TYPE.$CHR.bed
	done
	'
	to
	'
	for TYPE in protein_coding processed_pseudogene lncRNA
	do
	    echo "--- Creating $TYPE.$CHR.bed"
	    grep $TYPE $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="gene"){print $1, $4-1, $5}}' > $TYPE.$CHR.bed
	done
	'
3. The trends: most of the allele count tends to be under 1000. only a small amount of them are larger then 1000.

##exercise4 document for  bxlab/cmdb-plot-vcfs
###SYNOPSIS
1. this file contain scripts to deal with GTF file, combine it with known VCF file. Also to look at the allele count of different features, 
2. it will tell you how many bp does each feature (including exon, processed_pseudogene, protein_coding, and lncRNA) cover.
3. it will return bed and vcf files for each feature(including exon, processed_pseudogene, protein_coding, and lncRNA).
4. it will also return the histogram plot of the density of each feature's allele counts.
###USAGE
1. bash do_all.sh <thing1> <thing2>
	<thing1> the vcf file we need, like random_snippet.vcf
	<thing2> the gtf file we need, like chr21.gtf
		
###DEPENDENCIES
1. create the environment
	conda create --name day4-lunch
	conda activate day4-lunch
2. install bedtools and matplotlib
	conda install bedtools matplotlib
###DESCRIPTION
1. Create .bed files for features of interest
	- Run subset_regions.sh Bash script
	- Use grep to get the line with specific feature we want, like protein_coding, processed_pseudogene, lncRNA and exon
		exons are exons with protein-coding genetype, but not other exons