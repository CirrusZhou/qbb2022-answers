```
1.filter
reference:https://www.jianshu.com/p/08d74365c64f
samtools view -q 10 D2_Sox2_R1.bam -o D2_Sox2_R1.q10.bam
samtools view -q 10 D2_Sox2_R1_input.bam -o D2_Sox2_R1_input.q10.bam
samtools view -q 10 D2_Sox2_R2.bam -o D2_Sox2_R2.q10.bam
samtools view -q 10 D2_Sox2_R2_input.bam -o D2_Sox2_R2_input.q10.bam

2.look for the size of chromosome 17: NC_034586.1: 1..90M (89,975,685 nt)
thus the genoms size is -g 9e7
reference:https://www.ncbi.nlm.nih.gov/genome/gdv/browser/genome/?id=GCF_900094665.1
https://www.jianshu.com/p/edfe4ac6b085
macs2 callpeak -t D2_Sox2_R1.q10.bam -c D2_Sox2_R1_input.q10.bam -B -g 9e7 -n D2_Sox2_R1
macs2 callpeak -t D2_Sox2_R2.q10.bam -c D2_Sox2_R2_input.q10.bam -B -g 9e7 -n D2_Sox2_R2

3.use bedtools to intersect peaks:
reference:https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html
bedtools intersect -wa -a D2_Sox2_R1_peaks.narrowPeak -b D2_Sox2_R2_peaks.narrowPeak > intersect.narrowPeak

4.colocalization of Sox2 and Klf4
bedtools intersect -a D2_Klf4_peaks.bed -b intersect.narrowPeak > klf4_sox2_intersect.bed

Try to see how many overlapped peaks:
wc -l klf4_sox2_intersect.bed
41 klf4_sox2_intersect.bed

Try to see how many peaks for Klf4:
wc -l D2_Klf4_peaks.bed
60 D2_Klf4_peaks.bed
So the percentage is 40/60=66.7%

Try to see how peaks for Sox2:
wc -l intersect.narrowPeak
593 intersect.narrowPeak



5.scale the bedgraph file
python extra_data/scale_bdg.py  D2_Sox2_R1_treat_pileup.bdg scaled_D2_Sox2_R1.bdg
python extra_data/scale_bdg.py  D2_Klf4_treat.bdg scaled_D2_Klf4_treat.bdg
python extra_data/scale_bdg.py  D0_H3K27ac_treat.bdg scaled_D0_H3K27ac_treat.bdg
python extra_data/scale_bdg.py  D2_H3K27ac_treat.bdg scaled_D2_H3K27ac_treat.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2_Sox2_R1.bdg > croped_D2_Sox2_R1.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2_Klf4_treat.bdg > croped_D2_Klf4_treat.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D0_H3K27ac_treat.bdg > croped_D0_H3K27ac_treat.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2_H3K27ac_treat.bdg > croped_D2_H3K27ac_treat.bdg

6.sort the file by number and reformat
reference:https://www.runoob.com/linux/linux-comm-sort.html
sort -n -k 5 -r intersect.narrowPeak | head -300 > first_300.narrowPeak
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' first_300.narrowPeak > reformated_first_300.narrowPeak

7.samtools faidx
reference:https://www.jianshu.com/p/eb6ea655df0a
samtools faidx -r reformated_first_300.narrowPeak mm10.fa -o extracted_sequence

8.meme-chip
meme-chip -maxw 7 extracted_sequence
get memechip_out

9.look at the downloaded file
(meme) [~/qbb2022-answers/week5-homework $]cd motif_databases
(meme) [~/qbb2022-answers/week5-homework/motif_databases $]ls
ARABD		ECOLI		JASPAR		MOUSE		TFBSshape
CIS-BP_1.02	EUKARYOTE	MALARIA		PROKARYOTE	WORM
CIS-BP_2.00	FLY		METHYLCYTOSINE	PROTEIN		YEAST
CISBP-RNA	HUMAN		MIRBASE		RNA		motif_db.csv

10.scan for similar motif and extract KLF4 and SOX2 related
tomtom memechip_out/meme_out/meme.html motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme 

awk '/KLF4/ || /SOX2/ {print $0}' tomtom_out/tomtom.tsv > tomtom_KLF4_SOX2
```