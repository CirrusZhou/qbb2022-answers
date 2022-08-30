#!/usr/bin/env python3

# import our function
from bed_parser import parse_bed

# specify the file name
fname = "hg38_gencodev41_chr21.bed"

# run the function
bed = parse_bed(fname)

exon_num = []

for i in bed:
    exon_num.append(i[9])
    
exon_num.sort()
total = len(exon_num)
if type(total/2) ==float:
    answer = exon_num[int(total/2 + 0.5)]
else:
    answer = exon_num[int(total/2)]
print(f"There are {total} numbers in the exon_num list.")
print(f"The median should be the {total/2} th number in the list.")
print(f"Which should be {answer}")

#print(exon_num)

