import pandas as pd
import numpy as np
import scipy.stats as stats
import pylab as pl

df = pd.read_csv('stroopdata.csv')
print(df['Congruent'].describe())
h =sorted(df['Congruent'])
fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)      #use this to draw histogram of your data

pl.show()                   #use may also need add this 

print(df['Incongruent'].describe())
h =sorted(df['Incongruent'])
fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
pl.plot(h,fit,'-o')
pl.hist(h,normed=True)      #use this to draw histogram of your data

pl.show()                   #use may also need add this 

y = df['Congruent']
x = df['Incongruent']

bins = np.linspace(0, 40, 50)
pl.hold(True)
pl.hist(x, bins, alpha=0.5, label='x')
pl.hist(y, bins, alpha=0.5, label='y')
pl.legend(loc='upper right')
pl.show()
