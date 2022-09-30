```
1.index the genome:
bwa index sacCer3.fa

2.align sequence to the genome
bwa mem -R "@RG\tID:A01_09\tSM:A01_09" -o SRR16356854.sam c_elegans.PRJNA13758.WS283.genomic.fa.gz SRR16356854_1.subset.fastq.gz SRR16356854_2.subset.fastq.gz


Other see week3_hw.sh
```