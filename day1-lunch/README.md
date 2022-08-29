 # QBB2022 - Day 1 - Lunch Exercises Submission

1. I’m excited to learn bash.
 
2. Calculate the average number of exons per gene
 	a.
	cp ~/data/bed_files/genes.chr21.bed .
	cp ~/data/bed_files/exons.chr21.bed .
	
	b.
	grep chr21 exons.chr21.bed | wc -l
 	# count lines begin with chr21 to count exons in chr21
 	# the result I got: 13653
 
 	grep chr21 genes.chr21.bed | wc -l
 	# count lines begin with chr21 to count genes in chr21
 	# the result I got: 219
 
 	Thus, the mean number of exons per gene is 13653/219 = 62.34, which I will take 62 exons/gene
	
	c.I would see how many exons are in each gene by considering the genome scope(location), and then sort them to find the median!
 
3.Tally chromHMM states in E116 lymphoblastoid cells
 	a.
	cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
 	
	b.
	cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > state
	sort state | uniq -c
	 305 1
	  17 10
	  17 11
	  30 12
	  62 13
	 228 14
	 992 15
	 678 2
	  79 3
	 377 4
	 808 5
	 148 6
	1050 7
	 156 8
	 654 9
	 
	 c.
	 I would like to add a 5th column in the file, and add the (third col - second col) in this column.
	 Then, I will sort the file by 4th col, and calculate the sum of 5th cols which have the same state in 4th col.
	 Find the state with the largest sum.
	 
4.Tally populations among 1000 Genomes Project samples
	a.
	cp /Users/cmdb/data/metadata_and_txt_files/integrated_call_samples.panel .
	
	b.
	grep AFR integrated_call_samples.panel > AFR_super_pop
	cut -f 2 AFR_super_pop > AFR_pop
	sort AFR_pop | uniq -c
	
    123 ACB
    112 ASW
    173 ESN
    180 GWD
    122 LWK
    128 MSL
    206 YRI
	
	c.
	Repeat b for every super population!😂
	
	another way: remove the grep step and sort by superfamily.
	
	
5.
	a.
	cp /Users/cmdb/data/vcf_files/random_snippet.vcf .
	
	b.
	cut -f 1-9,13 random_snippet.vcf > HG00100.vcf
	
	c.
	sort -k 10 HG00100.vcf | cut -f 10 | uniq -c
	9514 0|0
	 127 0|1
	 178 1|0
	 181 1|1
	 
	d. 15 rows contain AF=1
	grep ";AF=1" random_snippet.vcf | wc -l
      15

    another way:
	cut -d ";" -f 4 random_snippet.vcf > AF
	sort AF | uniq -c
	 15 AF=1

	e. AF=1 appear once per row
	
	f. I would cut the file to get 7th col which is seperated by ";". Then I will get all AFR values.
	
 