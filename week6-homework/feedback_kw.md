## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1 + 1 + 1 = 12 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

6. Script set up to convert sparse data into square matrix

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

I think you want to remove the distance dependent signal for matrix1 and matrix2 separately

Then you want to smooth the signal (like you did) for matrix1 and matrix2 separately

Finally, you want to subtract, and you can do this without a for loop, just by doing matrix3 = matrix2 - matrix1

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

  * I see this plot

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

  * I don't see this plot --> +0
  * Should use the sparse data `/Users/cmdb/qbb2022-answers/week6-homework/matrix/dCTCF_full.6400.matrix` and `/Users/cmdb/qbb2022-answers/week6-homework/matrix/ddCTCF_full.6400.matrix`; and the bin data `/Users/cmdb/qbb2022-answers/week6-homework/matrix/6400_bins.bed` from the `3dgenome_data.tar.gz` file.

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?

    * sequencing depth shouldn't influence bin size, but it does influence how noisy/cohesive the TADs signal looks together on a plot.

  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

You only need to read in data for the dCTCF_full.40000.matrix, not the dCTCF_ontarget_6400_iced.matrix

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)
