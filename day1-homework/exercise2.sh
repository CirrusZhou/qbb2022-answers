chromHMM=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed
vcffile=~/data/vcf_files/random_snippet.vcf

bedtools intersect -a $chromHMM -b $vcffile > intersect_out.bed

