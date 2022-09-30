for SAMPLE in *fastq
do
	bwa mem \
	-R "@RG\tID:${SAMPLE}\tSM:${SAMPLE}" \
	-t 4 \
	-o ${SAMPLE}.sam sacCer3.fa ${SAMPLE}
done

for SAMPLE in *sam
do
	samtools sort -@ 4 -O bam -o ${SAMPLE}.bam ${SAMPLE}
done 

for SAMPLE in *bam
do
	samtools index $SAMPLE
done

freebayes -f sacCer3.fa --genotype-qualities -p 2 *bam| vcffilter -f "QUAL > 20" >freebayes.vcf



vcfallelicprimitives -k -g freebayes.vcf > pri_freebayes.vcf



snpeff ann R64-1-1.99 pri_freebayes.vcf > snp_freebayes.vcf

head -n 100 freebayes.vcf > week3_variant.vcf