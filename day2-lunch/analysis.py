#!/usr/bin/env python3

# import our function
from bed_parser import parse_bed

# specify the file name
fname = "hg38_gencodev41_chr21.bed"

# run the function and store the returned result in bed
bed = parse_bed(fname)

# create a list 
exon_num = []

# for everyline in bed
for i in bed:
    # get the exon number and append it into the list.
    exon_num.append(i[9])

# sort the list to find the median    
exon_num.sort()
# let's see how many numbers are in the list
total = len(exon_num)

# if the amount number is odd, just pick the middlemost number to be median
if type(total/2) ==float:
    answer = exon_num[int(total/2 + 0.5)]
# if the amount number is even, median is the average of the two middlemost numbers
else:
    answer = (exon_num[int(total/2)] + exon_num[int(total/2)+1])/2

# give the reader some feedback
print(f"There are {total} numbers in the exon_num list.")
print(f"The median should be the {total/2} th number in the list.")
print(f"Which should be {answer}")

#print(exon_num)

