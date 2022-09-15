# week1 homework

1. Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
	1000000 * 5 / 100 = 50000 reads for 5x coverage
	1000000 * 15 / 100 = 150000 reads for 15x coverage
	
2. Question 1.2 
	See exercise 1_2.png

3. Question 1.3. Using your output array of coverages from Q1.2, how much of the genome (e.g., how many base pairs) has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?
	
	run the simulation several times. Seems good.
	```
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  7255
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  7013
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  6875
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  6405
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  6608
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  6639
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  7262
	0 coverage bp in poisson distribution:  6737.946999085467
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  7042
	0 coverage bp in poisson distribution:  6737.946999085467
	```

4. Question 1.4. Now repeat the analysis with 15x coverage: 
	See exercise 1_4.png
	
	run the simulation several times. Seems good.
	```
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  16
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  14
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  24
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  8
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  4
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  3
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  5
	0 coverage bp in poisson distribution:  0.3059023205018258
	(base) [~/qbb2022-answers/week1-homework $]python class1.py 
	0 coverage bp in simulation:  6
	0 coverage bp in poisson distribution:  0.3059023205018258
	```
	
5. Question 2. De novo assembly
	download the spades
	```
	curl http://cab.spbu.ru/files/release3.15.5/SPAdes-3.15.5-Darwin.tar.gz -o SPAdes-3.15.5-Darwin.tar.gz
    tar -zxf SPAdes-3.15.5-Darwin.tar.gz
    cd SPAdes-3.15.5-Darwin/bin/
	```
	
	the pathway of spades.py is 
	```
	/Users/cmdb/SPAdes-3.15.5-Darwin/bin
	```
	
	run the spades(reference: http://sepsis-omics.github.io/tutorials/modules/spades_cmdline/#:~:text=Assemble%20Run%20Spades%3A%20spades.py%20-1%20illumina_R1.fastq.gz,-2%20illumina_R2.fastq.gz%20--careful%20--cov-cutoff%20auto%20-o%20spades_assembly_all_illumina)
	```
	/Users/cmdb/SPAdes-3.15.5-Darwin/bin/spades.py -1 frag180.1.fq -2 frag180.2.fq --careful --cov-cutoff auto -o contig_frag180
	/Users/cmdb/SPAdes-3.15.5-Darwin/bin/spades.py -1 jump2k.1.fq -2 jump2k.2.fq --careful --cov-cutoff auto -o contig_jump2k
	
	-1 is input file of forward reads
	-2 is input file of reverse reads
	--careful minimizes mismatches and short indels
	--cov-cutoff auto computes the coverage threshold (rather than the default setting, “off”)
	-o is the output directory
	
	```
	
6. Question 2.1. How many contigs were produced? [Hint: try grep -c '>' contigs.fasta]

	for frag_180, there are 4 contigs
	```
	(base) [~/qbb2022-answers/week1-homework/asm/contig_frag180 $]grep -c '>' contigs.fasta
	4
	```
	
	for jump2k, there are 9 contigs
	```
	(base) [~/qbb2022-answers/week1-homework/asm/contig_jump2k $]grep -c '>' contigs.fasta
	9
	```
	
7. Question 2.2. What is the total length of the contigs? [Hint: try samtools faidx, plus a short script if necessary]
	for frag_180:
	```
	samtools faidx contigs.fasta
	awk '{(total+=$2)};END{print total}' contigs.fasta.fai
	234467
	```
	
	for jump2k:
	```
	samtools faidx contigs.fasta
	awk '{(total+=$2)};END{print total}' contigs.fasta.fai
	234644
	```
	
8. Question 2.3. What is the size of your largest contig? [Hint: check samtools faidx plus sort -n]
	for frag_180:
	```
	awk '{print $2}' contigs.fasta.fai | sort -n | awk 'END {print}' 
	105830
	```


	for jump2k:
	```
	awk '{print $2}' contigs.fasta.fai | sort -n | awk 'END {print}' 
	93141
	```
	
9. Question 2.4. What is the contig N50 size? [Hint: Write a short script if necessary]

	for frag_180: 40k
	```
	awk '{print $2}' contigs.fasta.fai | sort -n 
	39426
	41351
	47860
	105830
	```
	
	for jump2k: 7k
	```
	awk '{print $2}' contigs.fasta.fai | sort -n
	51
	67
	67
	5713
	6955
	39440
	41347
	47863
	93141
	```
	
10. Question 3.1. What is the average identify of your assembly compared to the reference? [Hint: try dnadiff]
	100%

	downgrade the mummer
	```
	conda install mummer=3.23=h6de7cb9_11
	
	(reference:https://www.jianshu.com/p/c12f2a117892)
	nucmer  --prefix jump2k /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/contig_jump2k/contigs.fasta
	dnadiff -d jump2k.delta
	
	nucmer  --prefix frag_180 /Users/cmdb/qbb2022-answers/week1-homework/asm/ref.fa /Users/cmdb/qbb2022-answers/week1-homework/asm/contig_frag180/contigs.fasta
	dnadiff -d frag_180.delta
	```
	
	Output will be...
	   out.report  - Summary of alignments, differences and SNPs
	   out.delta   - Standard nucmer alignment output
	   out.1delta  - 1-to-1 alignment from delta-filter -1
	   out.mdelta  - M-to-M alignment from delta-filter -m
	   out.1coords - 1-to-1 coordinates from show-coords -THrcl .1delta
	   out.mcoords - M-to-M coordinates from show-coords -THrcl .mdelta
	   out.snps    - SNPs from show-snps -rlTHC .1delta
	   out.rdiff   - Classified ref breakpoints from show-diff -rH .mdelta
	   out.qdiff   - Classified qry breakpoints from show-diff -qH .mdelta
	   out.unref   - Unaligned reference sequence IDs and lengths
	   out.unqry   - Unaligned query sequence IDs and lengths
	

11. Question 3.2. What is the length of the longest alignment [Hint: try nucmer and show-coords]
	
	for jump2k, 93141 
	
	```
	delta-filter  -1 jump2k.delta > jump2k.delta.filter
	show-coords -r jump2k.delta.filter > jump2k.coord
	less -S jump2k.coord
	```
	
	see output format here:http://mummer.sourceforge.net/manual/#coords
	```
	    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
	=====================================================================================
	       6    26789  |    41347    14564  |    26784    26784  |   100.00  | Halomonas    NODE_5_length_41347_cov_9.661301
	   26788    40640  |    13853        1  |    13853    13853  |   100.00  | Halomonas    NODE_5_length_41347_cov_9.661301
	   40650    88512  |        1    47863  |    47863    47863  |   100.00  | Halomonas    NODE_3_length_47863_cov_9.855635
	   88518   127957  |    39440        1  |    39440    39440  |   100.00  | Halomonas    NODE_4_length_39440_cov_10.188469
	  127959   221099  |        1    93141  |    93141    93141  |   100.00  | Halomonas    NODE_7_length_93141_cov_10.054464
	  221085   221151  |        1       67  |       67       67  |   100.00  | Halomonas    NODE_2_length_67_cov_8.294118
	  221119   226831  |        1     5713  |     5713     5713  |   100.00  | Halomonas    NODE_8_length_5713_cov_9.984507
	  226817   226883  |       67        1  |       67       67  |   100.00  | Halomonas    NODE_9_length_67_cov_7.764706
	  226851   233805  |        1     6955  |     6955     6955  |   100.00  | Halomonas    NODE_6_length_6955_cov_8.581190
	```
	
	
	for frag_180, 105830 
	```
	delta-filter  -1 frag_180.delta > frag_180.delta.filter
	show-coords -r frag_180.delta.filter > frag_180.coord
	less -S frag_180.coord
	
	    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
	=====================================================================================
	       3    26789  |    41351    14565  |    26787    26787  |   100.00  | Halomonas    NODE_3_length_41351_cov_13.313130
	   26788    40641  |    13854        1  |    13854    13854  |   100.00  | Halomonas    NODE_3_length_41351_cov_13.313130
	   40651    88510  |    47860        1  |    47860    47860  |   100.00  | Halomonas    NODE_2_length_47860_cov_13.213367
	   88532   127957  |    39426        1  |    39426    39426  |   100.00  | Halomonas    NODE_4_length_39426_cov_13.187473
	  127965   233794  |        1   105830  |   105830   105830  |   100.00  | Halomonas    NODE_1_length_105830_cov_13.379475
	```
	
	
	
	
12. Question 3.3. How many insertions and deletions are in the assembly? [Hint: try dnadiff]

	For jump2k, in the out.report, we could find 1 insertions and 5 deletions.
	```
	Insertions                         5                    1
	InsertionSum                      21                  712
	InsertionAvg                    4.20               712.00
	```
	
	For frag_180, in the out.report, we could find 1 insertion and 5 deletions.
	```
	Insertions                         5                    1
	InsertionSum                      51                  712
	InsertionAvg                   10.20               712.00
	
	```
	
	Insertions     - Rough count of insertion events. Note that this is
	                 slightly different from "UnalignedBases" because it
	                 counts duplications as insertions, whereas
	                 UnalignedBases does not. Also, this count does not
	                 included sequences that have no alignments as
	                 insertions, whereas UnalignedBases does. Note than
	                 insertions in R can be viewed as deletions from Q.
	                 This number reports only "major" insertions defined
	                 as insertions large enough to break an alignment.
	                 Nucmer will align through smaller insertions of less
	                 than ~60 bases. These smaller insertions are
	                 reported in the "Indels" count below.


	mummerplot --png jump2k.delta.filter
	
13. Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. [Hint: try show-coords]
	Question 4.2. How long is the novel insertion? [Hint: try show-coords]

	for frag_180:
	The insertion is at NODE_3_length_41351_cov_13.313130 13855-14564
	corresponding position in reference is between 26788 and 26789

	
	```
	    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
	=====================================================================================
	       3    26789  |    41351    14565  |    26787    26787  |   100.00  | Halomonas    NODE_3_length_41351_cov_13.313130
	   26788    40641  |    13854        1  |    13854    13854  |   100.00  | Halomonas    NODE_3_length_41351_cov_13.313130
	   40651    88510  |    47860        1  |    47860    47860  |   100.00  | Halomonas    NODE_2_length_47860_cov_13.213367
	   88532   127957  |    39426        1  |    39426    39426  |   100.00  | Halomonas    NODE_4_length_39426_cov_13.187473
	  127965   233794  |        1   105830  |   105830   105830  |   100.00  | Halomonas    NODE_1_length_105830_cov_13.379475

	
	NODE_1_length_105830_cov_13.379475      105830  36      60      61
	NODE_2_length_47860_cov_13.213367       47860   107665  60      61
	NODE_3_length_41351_cov_13.313130       41351   156358  60      61
	NODE_4_length_39426_cov_13.187473       39426   198434  60      61
	
	```
	
	
	for jump2k: 
	The insertion is at NODE_5_length_41347_cov_9.661301 13854-14563
	corresponding position in reference is between 26788 and 26789
	

	
	```


	    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
	=====================================================================================
	       6    26789  |    41347    14564  |    26784    26784  |   100.00  | Halomonas    NODE_5_length_41347_cov_9.661301
	   26788    40640  |    13853        1  |    13853    13853  |   100.00  | Halomonas    NODE_5_length_41347_cov_9.661301
	   40650    88512  |        1    47863  |    47863    47863  |   100.00  | Halomonas    NODE_3_length_47863_cov_9.855635
	   88518   127957  |    39440        1  |    39440    39440  |   100.00  | Halomonas    NODE_4_length_39440_cov_10.188469
	  127959   221099  |        1    93141  |    93141    93141  |   100.00  | Halomonas    NODE_7_length_93141_cov_10.054464
	  221085   221151  |        1       67  |       67       67  |   100.00  | Halomonas    NODE_2_length_67_cov_8.294118
	  221119   226831  |        1     5713  |     5713     5713  |   100.00  | Halomonas    NODE_8_length_5713_cov_9.984507
	  226817   226883  |       67        1  |       67       67  |   100.00  | Halomonas    NODE_9_length_67_cov_7.764706
	  226851   233805  |        1     6955  |     6955     6955  |   100.00  | Halomonas    NODE_6_length_6955_cov_8.581190
	
	  NODE_1_length_51_cov_24.000000  51      32      51      52
	  NODE_2_length_67_cov_8.294118   67      115     60      61
	  NODE_3_length_47863_cov_9.855635        47863   218     60      61
	  NODE_4_length_39440_cov_10.188469       39440   48914   60      61
	  NODE_5_length_41347_cov_9.661301        41347   89046   60      61
	  NODE_6_length_6955_cov_8.581190 6955    131116  60      61
	  NODE_7_length_93141_cov_10.054464       93141   138222  60      61
	  NODE_8_length_5713_cov_9.984507 5713    232949  60      61
	  NODE_9_length_67_cov_7.764706   67      238789  60      61
	
	```

14. Question 4.3. What is the DNA sequence of the encoded message? [Hint: try samtools faidx to extract the insertion]
	
	for frag_180:
	```
	samtools faidx /Users/cmdb/qbb2022-answers/week1-homework/asm/contig_frag180/contigs.fasta NODE_3_length_41351_cov_13.313130:13855-14564 > insertion_frag180.fa
	```
	The sequence is :
	```
	>NODE_3_length_41351_cov_13.313130:13855-14564
	ACTAGTTCCCGATTGCACGCGTACTTCAAGTCCCGAATAGAGTACTCTTCTAAGTGACTA
	AGCTGTTCCGTGGTTCGTGCACTCAGCTCGTAAGAGAGGCCTTATGCAAGACAGTCATGT
	TTTCGGATATGAATTGCCGACTGGCTCACTTGAGCAATATGCTCAGGTACGAATGTTTGA
	GGTCGGACATACCCGCAGTAATTCATGTTTTCGGAAAGGAATGCCCGCAGCTTCGACTCC
	TCGCCGCCCAGCAGAAACTCATGTCCGCCTGGGGTCGTGCAAGACTACAAGCATGTGTTA
	TGTGTGCAAGCGAGTCCGATAGGACTACGCTGCTGGTTTCGTTTGGTCGGCGTTGAGGAC
	TTACCGCAGTACAGCGTTTCAGTTAATAATAAGTTCCTTTTGTCTGAGCGCTATTGGCTG
	AGGCGATGAGGTGGGCTTGGGTGGATGTGGTCTTGCTTGGCTGGAGTGCTCGCCTTAGCA
	GGGTAGTTGTGAGGTATGCCGTTAGGCCGGTGGGCCGTTCTGCAGGTTGGTCGTAGAGTA
	CTTGGATAAGTTATCAATGTTGTAGTAAAAGAATTGAGCCATTGGGTATGAATGCCATGC
	CCTCCTCCAATAAGAGGCTAATGGATAAAGCGGTGCCTTGCATCCGATAGAACGTGATCA
	CTCTTTGCCGTCTGCCCTCCCGTAAGGCCATACTACAATACGCATTGTAT
	```
	
	for jump2k:
	```
	samtools faidx /Users/cmdb/qbb2022-answers/week1-homework/asm/contig_jump2k/contigs.fasta NODE_5_length_41347_cov_9.661301:13854-14563 > insertion_jump2k.fa
	```	
	The sequence is :
	```
	>NODE_5_length_41347_cov_9.661301:13854-14563
	ACTAGTTCCCGATTGCACGCGTACTTCAAGTCCCGAATAGAGTACTCTTCTAAGTGACTA
	AGCTGTTCCGTGGTTCGTGCACTCAGCTCGTAAGAGAGGCCTTATGCAAGACAGTCATGT
	TTTCGGATATGAATTGCCGACTGGCTCACTTGAGCAATATGCTCAGGTACGAATGTTTGA
	GGTCGGACATACCCGCAGTAATTCATGTTTTCGGAAAGGAATGCCCGCAGCTTCGACTCC
	TCGCCGCCCAGCAGAAACTCATGTCCGCCTGGGGTCGTGCAAGACTACAAGCATGTGTTA
	TGTGTGCAAGCGAGTCCGATAGGACTACGCTGCTGGTTTCGTTTGGTCGGCGTTGAGGAC
	TTACCGCAGTACAGCGTTTCAGTTAATAATAAGTTCCTTTTGTCTGAGCGCTATTGGCTG
	AGGCGATGAGGTGGGCTTGGGTGGATGTGGTCTTGCTTGGCTGGAGTGCTCGCCTTAGCA
	GGGTAGTTGTGAGGTATGCCGTTAGGCCGGTGGGCCGTTCTGCAGGTTGGTCGTAGAGTA
	CTTGGATAAGTTATCAATGTTGTAGTAAAAGAATTGAGCCATTGGGTATGAATGCCATGC
	CCTCCTCCAATAAGAGGCTAATGGATAAAGCGGTGCCTTGCATCCGATAGAACGTGATCA
	CTCTTTGCCGTCTGCCCTCCCGTAAGGCCATACTACAATACGCATTGTAT
	
15. Question 4.4. What is the secret message? [Hint: Run the provided script dna-decode.py to decode the string from 4.3.]
	```
	python dna-decode.py --decode --input insertion_frag180.fa
	The decoded message :  ..,Æ%e§%çî%efÄgíg'GE§'îÄ&gìf%¤¤$''î$'ïÅed·ïíìÄÅç$çíW¶·ï÷î÷u4÷îÎÏÎÏíg§Gì'GìÆ$%§Eç%GEæÄf$$
	```