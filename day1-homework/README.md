# QBB2022 - Day 1 - Homework Exercises Submission

1.
	a. for the original script, I saw awk: illegal field $(), name "nuc". I search it in google and find there is sth wrong when we want to transfer the variable into awk. according to https://stackoverflow.com/questions/19845374/variable-set-used-by-awk-in-bash, we need to add -v nuc="$nuc" to transfer variable into awk, or we could put nuc="$nuc" outside awk
	
	b.the result:
	Considering  A
	 354 C
	1315 G
	 358 T
	Considering  C
	 484 A
	 384 G
	2113 T
	Considering  G
	2041 A
	 405 C
	 485 T
	Considering  T
	 358 A
	1317 C
	 386 G
	
	c.the result shows that A and G are more frequently replaced by each other, and the same to C and T. 
	This result make sense, since A and G are all purines, which have similar structure. there may be enzymes to convert them to each other. The same, C and T are all pyrimidines.
	In a word, transition occurs more easily than transversion.

2. What’s the most common alternate allele for a Cytosine reference allele for variants occurring in promoter like regions of the genome?
	a. 
	in all the 15 segmentations, promoters are not clearly and objectively defined. For me, I will take state 1, 2, 10, 11,  as promoter like regions.
	
	b.
	cp ~/data/vcf_files/random_snippet.vcf .
	cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
	
	awk '{if ($4 ==1 || $4 == 2 || $4 == 10 || $4 == 11){print} }' chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > chromHMM.bed
	
	bedtools intersect -wo -a chromHMM.bed -b random_snippet.vcf > intersect_out.bed
	awk '/^#/{next} {if ($8 == "C") {print $9}}' intersect_out.bed | sort | uniq -c
    
	12 A
    11 G
    39 T
	
	Thus T is the most common alternate allele for C reference allele for variants occurring in promoter like regions of the genome.
	
	c.
	Hypothesis:  C in promoter like regions is more likely to transit to T compared with transvert to A and G
	
3. 
	a.
	awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
	The first line manage the document by only taking useful message: the chromosome, the start position, and the end position. We create the start position by $2-1, in order to get a bed format, which is required by bedtool closest.
	
	sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
	This command line sorts the gene file by chromosome and then position. 2n means sort by 2nd col numerically.
	
	bedtools closest -a variants.bed -b genes.sorted.bed
	This command line find the closest gene around all variants.
	
	b.
	ERROR 1:
	(base) [~/qbb2022-answers/day1-homework $]bash exercise3.sh random_snippet.vcf
	Error: unable to open file or unable to determine types for file variants.bed

	- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
	- Also ensure that your file has integer chromosome coordinates in the 
	  expected columns (e.g., cols 2 and 3 for BED).
	  
	It seems our file is not TAB delimited.
	add this command:
	cat variants.bed|tr  " " "\t" > variants2.bed
	
	ERROR 2:
	Error: Sorted input specified, but the file variants2.bed has the following out of order record
	chr21	5218156	5218157
	
	The file variant2.bed is not sorted. So add this command:
	sort -k 2n variants2.bed > variants2.sorted.bed
	
	c.
	bash exercise3.sh random_snippet.vcf > result_exercise3
	
	wc -l result_exercise3
	   10293 result_exercise3
	10293 variants are involved.
	
	cut -f 7 result_exercise3|sort | uniq | wc -l
     200
	200 genes are involved
	
	Onaverage, 10293/200=51.465 variants are linked to a gene.
	
	