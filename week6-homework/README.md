1.What percentage of reads are valid interactions (duplicates do not count as valid)?
92% for dCTCF
88% for ddCTCF

2.What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?
dangling_end_pairs, religation_pair, self_cycle_pairs, single-end pairs, filtered_pairs, dumped_pairs
Dangling end, i.e. unligated fragments (both reads mapped on the same restriction fragment)
Self circles, i.e. fragments ligated on themselves (both reads mapped on the same restriction fragment in inverted orientation
Religation, i.e. ligation of juxtaposed fragments
Dumped pairs, i.e. any pairs that do not match the filtering criteria on inserts size, restriction fragments size or for which we were not able to reconstruct the ligation product.
single-end pairs?
filtered_pairs: 



3.see the data path and format
For dCTCF:

use the following as sparse data:
/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix 

use the following as bin file:
/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed

For ddCTCF:

use the following as sparse data:
/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix 

use the following as bin file:
/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/raw/6400/ddCTCF_ontarget_6400_abs.bed


dCTCF:
[(343068, 343068, 2459.883712) (343068, 343069,   56.278358)
 (343068, 343070,   63.640997) ... (343206, 343206, 2242.670835)
 (343206, 343207,  284.095217) (343207, 343207, 2045.943005)]

ddCTCF:
[(343068, 343068, 2288.050583) (343068, 343069,   51.607739)
 (343068, 343070,   39.279041) ... (343206, 343206, 2135.325912)
 (343206, 343207,  179.750115) (343207, 343207, 1966.715777)]

4.Were you able to see the highlighted difference from the original figure?
There is a shift in TADs, maybe due to the difference in beginning bin and end bin.

5.What impact did sequencing depth have?
Sequence depth will influence the resolution of Hi-C result. higher depth gives higher resolution and smaller bin size.

6.Highted signal means strong indication of interaction between two locations. High signal in the difference map means CTCF function influence the interaction between these two locations. With CTCF, these interaction will be blocked. Without CTCF, interaction will appear.

