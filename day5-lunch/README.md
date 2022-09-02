#Day5-lunch

##exercise 1
1. the data in aau1043_dnm.csv looks like:
	Chr,Pos,Ref,Alt,Proband_id,Phase_combined,Crossover,Sanger
	chr1,241097646,C,T,99379,father,paternal_crossover,confirmed
	chr10,29202943,A,G,8147,father,maternal_crossover,PCR failed
	chr11,129441657,C,T,5410,mother,maternal_crossover,confirmed
	chr13,96867147,A,G,46025,father,paternal_crossover,confirmed
	chr17,50609998,C,T,144769,mother,maternal_crossover,confirmed

	~first we count all father and mother
	```grep -v "Chr" aau1043_dnm.csv | cut -d "," -f 5 |sort|uniq -c > all_count```
	~then we count only father
	```grep -v "Chr" aau1043_dnm.csv |grep  "father" | cut -d "," -f 5 |sort|uniq -c > paternal_count```
    72 100770
    70 101199
    55 101332
    53 102060
    55 102313
    77 102727
	~and count only mother
	```
	grep -v "Chr" aau1043_dnm.csv |grep "mother" | cut -d "," -f 5 |sort|uniq -c > maternal_count
    12 100770
    16 101199
    30 101332
     8 102060
    28 102313
	```
	~then we join father and mother count into one file
	```
	join -1 2 -2 2 -o 1.2,1.1,2.1 paternal_count maternal_count > joined_count
	
	100770 72 12
	101199 70 16
	101332 55 30
	102060 53 8
	102313 55 28
	102727 77 14
	103818 45 17
	104333 46 15
	104502 57 11
	```

2. let's see how does aau1043_parental_age.csv look like:
	Proband_id,Father_age,Mother_age
	675,31,36
	1097,19,19
	1230,30,28
	1481,32,20
	1806,38,34
	2280,38,20
	3190,35,25
	3212,23,19
	
	
	grep -v "Proband_id" aau1043_parental_age.csv | cat | tr ',' ' ' > aau1043_parental_age.txt
	675 31 36
	1097 19 19
	1230 30 28
	1481 32 20
	1806 38 34
	2280 38 20
	3190 35 25
	3212 23 19
	3450 25 22
	3578 23 20
	3723 32 30
	
	~join the file together according to the proband_id
	```join -1 1 -2 1 <(sort joined_count) <(sort aau1043_parental_age.txt) > age_count
	
	101199 70 16 29 30
	101332 55 30 37 33
	102060 53 8 25 22
	102313 55 28 30 35
	102727 77 14 39 32
	103818 45 17 20 22
	```
	~let us check whether we are right 
	```
	(base) [~/qbb2022-answers/day5-lunch $]grep "101199" joined_count
	101199 70 16
	(base) [~/qbb2022-answers/day5-lunch $]grep "101199" aau1043_parental_age.txt
	101199 29 30
	(base) [~/qbb2022-answers/day5-lunch $]grep "101199" age_count
	101199 70 16 29 30
	```
	
	Looks great!


## exercise 2	
1. test for an association between maternal age and maternally inherited de novo mutations
	==============================================================================
	Dep. Variable:                m_count   R-squared:                       0.228
	Model:                            OLS   Adj. R-squared:                  0.226
	Method:                 Least Squares   F-statistic:                     116.0
	Date:                Fri, 02 Sep 2022   Prob (F-statistic):           6.88e-24
	Time:                        13:57:11   Log-Likelihood:                -1158.1
	No. Observations:                 396   AIC:                             2320.
	Df Residuals:                     394   BIC:                             2328.
	Df Model:                           1                                         
	Covariance Type:            nonrobust
	==============================================================================
	                 coef    std err          t      P>|t|      [0.025      0.975]
	------------------------------------------------------------------------------
	Intercept      2.5040      0.981      2.553      0.011       0.576       4.432
	m_age          0.3776      0.035     10.772      0.000       0.309       0.446
	==============================================================================
	Omnibus:                       51.143   Durbin-Watson:                   2.141
	Prob(Omnibus):                  0.000   Jarque-Bera (JB):               75.501
	Skew:                           0.845   Prob(JB):                     4.03e-17
	Kurtosis:                       4.310   Cond. No.                         121.
	==============================================================================
	
	The relationship is significant. 
	The size of this relationship is 0.3776

2. test for an association between paternal age and paternally inherited de novo mutations.
	==============================================================================
	Dep. Variable:                f_count   R-squared:                       0.619
	Model:                            OLS   Adj. R-squared:                  0.618
	Method:                 Least Squares   F-statistic:                     639.6
	Date:                Fri, 02 Sep 2022   Prob (F-statistic):           1.55e-84
	Time:                        13:57:32   Log-Likelihood:                -1406.6
	No. Observations:                 396   AIC:                             2817.
	Df Residuals:                     394   BIC:                             2825.
	Df Model:                           1                                         
	Covariance Type:            nonrobust
	==============================================================================
	                 coef    std err          t      P>|t|      [0.025      0.975]
	------------------------------------------------------------------------------
	Intercept     10.3263      1.702      6.066      0.000       6.979      13.673
	f_age          1.3538      0.054     25.291      0.000       1.249       1.459
	==============================================================================
	Omnibus:                        7.687   Durbin-Watson:                   1.907
	Prob(Omnibus):                  0.021   Jarque-Bera (JB):                8.185
	Skew:                           0.256   Prob(JB):                       0.0167
	Kurtosis:                       3.483   Cond. No.                         127.
	==============================================================================

	The relationship is significant. 
	The size of this relationship is 1.3538
	
3. They are significantly different
	Ttest_indResult(statistic=-53.40356528726923, pvalue=2.198603179308129e-264)
	
4.   warnings.warn('nan values have been dropped', ValueWarning)
	0    78.018535
	dtype: float64
	
	the predicted value maybe 78.018535