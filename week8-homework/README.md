
conda create -n medaka medaka
conda activate medaka
medaka_variant -h

1.medaka_variant -i methylation.bam -r "chr11:1900000-2800000" -f hg38.fa -p chr11_variant
medaka_variant -i methylation.bam	-r "chr14:100700000-100990000" -f hg38.fa -p chr14_variant
medaka_variant -i methylation.bam	-r "chr15:23600000-25900000" -f hg38.fa -p chr15_variant
medaka_variant -i methylation.bam	-r "chr20:58800000-58912000" -f hg38.fa -p chr20_variant

medaka_variant -i methylation.bam -r "chr11:1900000-2800000" -f hg38.fa -o chr11_variant  -p chr11_variant.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr14:100700000-100990000" -o chr14_variant  -p chr14_variant.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr15:23600000-25900000" -o chr15_variant  -p chr15_variant.vcf
medaka_variant -i methylation.bam -f hg38.fa -r "chr20:58800000-58912000" -o chr20_variant  -p chr20_variant.vcf

2.sudo /usr/bin/xcode-select --install

3.
whatshap haplotag -o chr11_tag -r hg38.fa --regions chr11:1900000:2800000 --output-haplotag-list chr11_list chr11_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr14_tag -r hg38.fa --regions chr14:100700000:100990000 --output-haplotag-list chr14_list chr14_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam


whatshap haplotag -o chr15_tag -r hg38.fa --regions chr15:23600000:25900000 --output-haplotag-list chr15_list chr15_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam
whatshap haplotag -o chr20_tag -r hg38.fa --regions chr20:58800000:58912000 --output-haplotag-list chr20_list chr20_variant/round_0_hap_mixed_phased.vcf.gz methylation.bam



4.
whatshap split chr11_tag chr11_list --output-h1 chr11_h1.bam --output-h2 chr11_h2.bam
whatshap split chr14_tag chr14_list --output-h1 chr14_h1.bam --output-h2 chr14_h2.bam
whatshap split chr15_tag chr15_list --output-h1 chr15_h1.bam --output-h2 chr15_h2.bam
whatshap split chr20_tag chr20_list --output-h1 chr20_h1.bam --output-h2 chr20_h2.bam

5.
samtools index chr11_h1.bam
samtools index chr11_h2.bam 
samtools index chr14_h1.bam
samtools index chr14_h2.bam
samtools index chr15_h1.bam
samtools index chr15_h2.bam
samtools index chr20_h1.bam
samtools index chr20_h2.bam

6.
Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.
Yes, because the file split is according to the tag assigned before. H1 always have the same tag, which should be mother, and H2 should always be the father.

7.
