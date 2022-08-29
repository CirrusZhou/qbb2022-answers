#!/bin/bash

#USAGE: bash exercise1.sh input_VCF
#for the original script, I saw awk: illegal field $(), name "nuc". I search it in google and find there is sth wrong when we want to transfer the variable into awk. according to https://stackoverflow.com/questions/19845374/variable-set-used-by-awk-in-bash, we need to add -v nuc="$nuc" to transfer variable into awk, or we could put nuc="$nuc" outside awk

for nuc in A C G T
do
  echo "Considering " $nuc
  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c
done

:'the result:
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
'

# the result shows that A and G are more frequently replaced by each other, and the same to C and T. 
# this result make sense, since A and G are all purines, which have similar structure. there may be enzymes to convert them to each other. The same, C and T are all pyrimidines.