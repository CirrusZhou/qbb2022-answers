#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
cat variants.bed|tr  " " "\t" > variants2.bed
sort -k 2n variants2.bed > variants2.sorted.bed
sort -k1,1 -k2,2n  ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants2.sorted.bed -b genes.sorted.bed
