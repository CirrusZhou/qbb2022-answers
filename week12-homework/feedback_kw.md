## Week 13

0 + 1 + 1 + 1 + 0.5 + 1 + 1 + 1 + 1 + 1 = 8.5 out of 10 points possible

1. Wright Fisher simulation is a function

  * not a function

2. simulation uses starting allele frequency and population size as input

3. simulation uses `numpy.random.binomial` to draw allele count samples

4. simulation stops when one allele is fixed

5. simulation returns a list of allele frequencies at each generation

  * where's the `frequency` list defined that you try to append to in the first `for` loop?

6. line plot generation number x-axis and allele frequency y-axis with notated starting allele frequency and pop size as well as labeled axes; 0.5 pts for notes/labels

7. time to fixation histogram for starting allele freq of 0.5 and pop size of 100 with at least 1000 independent runs

8. line plot for fixation time (y-axis) vs N (x-axis) for a starting allele frequency of 0.5 and varied population size (at least 6 different from 100 - 10mil). Label ticks

9. step 5 running the simulation for a range of 10 starting allele frequencies from 0 to 1. 100 simulations each

10. step 5 plot for variability in the time to fixation for each starting allele frequency. label the ticks and notate population size (0.5 pts for notes and labels)

Possible bonus points

1. Introduce selection in the simulation function

2. plot the allele frequency trajectory, notating selection coefficient, etc.

3. plot selection coefficient vs time to fixation for fixed population size, note population size on plot

**while the code doesn't meet the specifications we asked, it is good work.** I'd recommend using a while loop that checks to make sure p > 0 and p < 1 rather than a for loop with a large range that breaks. That range may cause the simulation to pre-maturely end depending on starting parameters
