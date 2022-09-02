#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels.api as sm

df = np.genfromtxt("age_count", delimiter = " ", dtype= None, encoding = None,names = ["ID","f_count","m_count","f_age","m_age"])
#print(df)

fig, ax  = plt.subplots()
ax.scatter(df["m_age"], df["m_count"],s=10)
ax.set_xlabel("mother age")
ax.set_ylabel("maternal mutation count")
#plt.show()
ax.title.set_text("the relationship between fother age and number of paternal mutations")
plt.savefig("ex2_a.png")
plt.close(fig)

fig, ax  = plt.subplots()
ax.scatter(df["f_age"], df["f_count"],s=10)
ax.set_xlabel("father age")
ax.set_ylabel("paternal mutation count")
ax.title.set_text("the relationship between mother age and number of maternal mutations")
plt.savefig("ex2_b.png")
plt.close(fig)

m_model = smf.ols(formula = "m_count ~ 1 + m_age ", data = df).fit()
#print(m_model.summary())

f_model = smf.ols(formula = "f_count ~ 1 + f_age ", data = df).fit()
#print(f_model.summary())

fig, ax  = plt.subplots()
ax.hist(df["f_count"], alpha = 0.5,label = "paternal")
ax.hist(df["m_count"], alpha = 0.5, label = "maternal")
ax.set_xlabel("Number of mutations")
ax.set_ylabel("Number of individuals")
ax.legend()
ax.title.set_text("number of maternal and paternal mutations in individuals ")
plt.savefig("ex2_c.png")

#print(stats.ttest_ind(df["m_count"],df["f_count"]))

new_data = df[0]
new_data.fill(0)
new_data['f_age'] = 50.5
print(f_model.predict(new_data))
