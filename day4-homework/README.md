# Day4 Homework

##Part A Expand simulation conditions
1. 
	```numpy.arange(0.55, 1.05, 0.05)```
	then we get
	```array([0.55, 0.6 , 0.65, 0.7 , 0.75, 0.8 , 0.85, 0.9 , 0.95, 1.  ])```
	so the 0.55 means the beginning, 1.05 means the ending, and 0.05 means the step length we take.
	
	```print(numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2))```
	gives us
	```[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]```
	It seems nothing has changed in our case. But I understand that numpy.around() give us the number with desired decimals.
	
	
	```print(numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1])```
	gives us the reversed array
	```[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]```
	
##Part C Plot
1. according to the heatmap, larger the prob (means more biased the prob, say, larger the real significance), larger the tosses (say, larger the sample size), then we get the larger power.


##Part D Compare to a real study
1. During miosis, Mendel's law of Segregation suggests that a diploid individual's offspring inherit heterozygous alleles with equal probability. However, there are violations of Mendel's law of segregation, leading to "transmission distortion", meaning that some allele are more likely to be passed to offspring than the others. However, we do not know whether this phenomenon exists in humans because of the small family size. This study is focusing on revisiting this question using single-cell sequencing data from individual human sperm with unprecedented statistical power.

2. Generally, we all use binomial test to analyze our data, and we use a heatmap to show power of the test under different probabilities and sample sizes. 

	There are also some differences. Firstly, article's probability has max 0.7, we have max 1. Also, article's sample size is much larger than ours. Secondly, for the p-value corrected panel, they use a threshold of 1.78*10^-7, we still use 0.05. Thirdly, our x axis is in log scale, so the trend should be more significant

	Specifically, probability of heads corresponds to the transmission rate axis.  number of tosses corresponds to the Number of sperm axis
	
	Why both simulations use a binomial test? 
	because our data are all binomial distributed. For coin toss, we either get a head or a tail. For the allele in a sperm (from one individual), we either get the allele1 or the allele2, since one individual could have at most two alleles at one position.