from scipy import stats
from scipy.stats import poisson
import numpy as np
from random import *
a=[]
for i in range(10):
    a.append(uniform(-2,2))

y=stats.describe(a)


r = poisson.rvs(8, size=8)


print('Poisson distribution:')
for i in range(8):
    print(r[i],end=' ')
print()
print()
print('Normal distribution:')
print('Number of elements:',y[0])
print('Elements:')
print(a)
print('Minimum:{:.5f}'.format(y[1][0]),'Maximum:{:.5f}'.format(y[1][1]))
print('Mean:{:.5f}'.format(y[2]))
print('Variance:{:.5f}'.format(y[3]))
print('Skewness:{:.5f}'.format(y[4]))
print('Kurtosis:{:.5f}'.format(y[5]))
