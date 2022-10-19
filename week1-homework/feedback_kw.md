# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 0.5 + 1 + 0.5 + 0.5  = 8.5 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * --> +1

2. Question 1.2, 1.4 simulation script(s

  * fantastic job making the simulation code generalized for genome length and fragment length variables! Consider using a single script that accepts command line/user input or a function that you can pass these variables to --> +1

3. Question 1.2, 1.4 plotting script(s)

  * your method for plotting the Poisson distribution works. You could try using something like the example 2 in the following next time for smoother lines: https://www.geeksforgeeks.org/how-to-create-a-poisson-probability-mass-function-plot-in-python/
  * Note that your 1-2.py script saves the figure as exercise1_4.png
  * --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * good plots overall, you could add axis labels --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * good code! impressed that you ran the simulation several times to check if the comparison held multiple times --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  **Note: You shouldn't run spades separately for the two types of reads; you want to run them together like the following, which is also provided at the bottom of the assignment online; you don't need to redo this because your methods for answering questions are correct.**

  ```
  spades.py --pe1-1 asm/frag180.1.fq --pe1-2 asm/frag180.2.fq --mp1-1 asm/jump2k.1.fq --mp1-2 asm/jump2k.2.fq -o asm -t 4 -k 31
  ```

  * number of contigs --> +0.5
  * total length of contigs --> 0.5 -- great awk usage!

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> 0.5
  * contig n50 size --> +0, please be precise in your answer and provide your reasoning

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0; incorrect message but correct idea -  revisit the help message for the script and see if there's a flag that you can try using and see if the message makes more sense
