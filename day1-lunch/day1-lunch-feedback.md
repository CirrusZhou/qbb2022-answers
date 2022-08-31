Really good work throughout! A couple specific comments: 

3c. This is a great solution!

4c. It's a good thought use some clever sorting to solve this. However, if you sort by superpopulation, you just end up with counts for the 5 superpopulations, whereas we want to sort by population. The way to do this would be to cut out the population and superpopulation columns, and sort the unique combinations of those. The way to cut out the two columns would be: `cut -f 2,3`

5d. Good job on searching for ";AF=1" as a way of avoiding counting lines with strings such as "EUR_AF=1".

5e. You are right that there is only one reported value for the global allele frequency (AF), but AF=1 can also appear as part of superpopulation allele frequencies, ie as part of SAS_AF=1. 

- Andrew
