SRR492183_1.fastq	SRR492189_1.fastq	SRR492194_1.fastq
SRR492183_2.fastq	SRR492189_2.fastq	SRR492194_2.fastq
SRR492186_1.fastq	SRR492190_1.fastq	SRR492197_1.fastq
SRR492186_2.fastq	SRR492190_2.fastq	SRR492197_2.fastq
SRR492188_1.fastq	SRR492193_1.fastq
SRR492188_2.fastq	SRR492193_2.fastq

SRR492183.kraken	SRR492189.kraken	SRR492194.kraken
SRR492186.kraken	SRR492190.kraken	SRR492197.kraken
SRR492188.kraken	SRR492193.kraken	assembly.kraken

Parse using the code provided:
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
python parser.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197


The instructions for ktImporttext usage:
https://manpages.debian.org/testing/radiant/ktImportText.1.en.html

ktImportText SRR492183_krona.txt -q -o SRR492183.krona.html
Firmicutes --> Bacilli
ktImportText SRR492186_krona.txt -q -o SRR492186.krona.html
ktImportText SRR492188_krona.txt -q -o SRR492188.krona.html
ktImportText SRR492189_krona.txt -q -o SRR492189.krona.html
ktImportText SRR492190_krona.txt -q -o SRR492190.krona.html
ktImportText SRR492193_krona.txt -q -o SRR492193.krona.html
ktImportText SRR492194_krona.txt -q -o SRR492194.krona.html
ktImportText SRR492197_krona.txt -q -o SRR492197.krona.html

The trend: continous increase of bacteria diversity, like growing population of  staphylococcus and cutibacterium.



STEP2
index:
bwa index metagenomics_data/step0_givendata/assembly.fasta
alignment:
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq | samtools sort -o SRR492183.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492186_1.fastq metagenomics_data/step0_givendata/READS/SRR492186_2.fastq | samtools sort -o SRR492186.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492188_1.fastq metagenomics_data/step0_givendata/READS/SRR492188_2.fastq | samtools sort -o SRR492188.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492189_1.fastq metagenomics_data/step0_givendata/READS/SRR492189_2.fastq | samtools sort -o SRR492189.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492190_1.fastq metagenomics_data/step0_givendata/READS/SRR492190_2.fastq | samtools sort -o SRR492190.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492193_1.fastq metagenomics_data/step0_givendata/READS/SRR492193_2.fastq | samtools sort -o SRR492193.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492194_1.fastq metagenomics_data/step0_givendata/READS/SRR492194_2.fastq | samtools sort -o SRR492194.bam

bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq | samtools sort -o SRR492197.bam


step2D-run metaBAT2
less easy way: 
jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam
metabat2 -i metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins_dir/bin

Question 3A: get 6 bins

Question 3B: Each bin cover 0.3~0.7% of the total assembly.
0 has  55
total length is  2705023
1 has  78
total length is  2251850
2 has  8
total length is  1656034
3 has  37
total length is  1227903
4 has  13
total length is  2483660
5 has  6
total length is  2862852
Total assembly has  4103
total length is  38071686

Question 3C: the bin looks about right, becase the size of prokaryotic genome size ranges from 1000000 to 10000000 bp.

Question 3D: For contamination, I would check some known single copy gene. If it appear for many times, there may be contamination.
For completion, I would check the size, usually expecting it to be larger than 2Mb.

Question 4A:
bin1: Staphylococcus aureus subsp. aureus ST72 or CN1
bin2: Staphylococcus epidermidis RP62A
bin3: hard to say, maybe Tissierellia 
bin4: Staphylococcus haemolyticus JCSC1435
bin5: one kind of Actinobacteria
bin6: Enterococcus faecalis

root   55
cellular organisms   55
Bacteria   55
Terrabacteria group   55
Firmicutes   55
Bacilli   55
Bacillales   55
Staphylococcaceae   55
Staphylococcus   55
Staphylococcus aureus   55
Staphylococcus aureus subsp. aureus   55
Staphylococcus aureus subsp. aureus ST72   49
Staphylococcus aureus subsp. aureus CN1   49
Staphylococcus aureus subsp. aureus TCH60   2
Staphylococcus aureus subsp. aureus MRSA252   1
Staphylococcus aureus subsp. aureus JKD6159   1



root   78
cellular organisms   78
Bacteria   78
Terrabacteria group   78
Firmicutes   78
Bacilli   78
Bacillales   78
Staphylococcaceae   78
Staphylococcus   78
Staphylococcus epidermidis   77
Staphylococcus epidermidis RP62A   51
Staphylococcus epidermidis ATCC 12228   24
Staphylococcus aureus   1
Staphylococcus aureus subsp. aureus   1


root   8
cellular organisms   8
Bacteria   8
Terrabacteria group   8
Firmicutes   8
Tissierellia   5
Tissierellales   5
Peptoniphilaceae   5
Anaerococcus   3
Anaerococcus prevotii   3
Anaerococcus prevotii DSM 20548   3
Finegoldia   2
Finegoldia magna   2
Finegoldia magna ATCC 29328   2
Bacilli   1
Lactobacillales   1
Streptococcaceae   1
Streptococcus   1
Streptococcus anginosus group   1
Streptococcus anginosus   1
Streptococcus anginosus C238   1
Clostridia   2
Clostridiales   2
Clostridiaceae   2
Clostridium   2
Clostridium novyi   1
Clostridium novyi NT   1


root   37
cellular organisms   37
Bacteria   37
Terrabacteria group   37
Firmicutes   37
Bacilli   37
Bacillales   37
Staphylococcaceae   37
Staphylococcus   37
Staphylococcus haemolyticus   24
Staphylococcus haemolyticus JCSC1435   24
Staphylococcus epidermidis   7
Staphylococcus epidermidis RP62A   2
Staphylococcus epidermidis ATCC 12228   3
Staphylococcus aureus   6
Staphylococcus aureus subsp. aureus   6
Staphylococcus aureus subsp. aureus Mu50   1
Staphylococcus aureus subsp. aureus USA300   2
Staphylococcus aureus subsp. aureus 11819-97   1
Staphylococcus aureus subsp. aureus ST398   1
Staphylococcus aureus subsp. aureus MSSA476   1


root   13
cellular organisms   13
Bacteria   13
Terrabacteria group   13
Actinobacteria   26
Propionibacteriales   13
Propionibacteriaceae   13
Cutibacterium   13
Cutibacterium avidum   13
Cutibacterium avidum 44067   13


root   6
cellular organisms   6
Bacteria   6
Terrabacteria group   6
Firmicutes   6
Bacilli   6
Lactobacillales   6
Enterococcaceae   6
Enterococcus   6
Enterococcus faecalis   6
Enterococcus faecalis OG1RF   2
Enterococcus faecalis V583   2
Enterococcus faecalis str. Symbioflor 1   1
Enterococcus faecalis D32   1

Question 4B:
Compare the number of contigs one taxonomy has in the scaffold. Choose the one with the most contigs.
