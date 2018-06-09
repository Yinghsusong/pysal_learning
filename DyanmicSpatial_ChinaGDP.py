#coding:utf-8
import numpy as np
import pysal
import matplotlib.pyplot as plt

f = pysal.open(r'D:\pysal_task\data\China_GDP.csv')
pci = np.array([f.by_col[str(y)] for y in range(1993,2014)])
# Classic Markov######################################################

print(f'pci.shape:\n{pci.shape}')
# (21, 31)
print(f'per capita income for the first year:\n{pci[0,:]}')
plt.plot(pci[0,:])
plt.show()
# define the class of income
q5 = np.array([pysal.Quantiles(y).yb for y in pci]).transpose()

print(f'q5 shape:\n{q5.shape}')
# (31, 21)矩阵转置以后，每一列为年份，每一行为各个省份
plt.scatter(range(1,32),q5[:,0])
plt.title('GDP Class in 1993')
plt.ylabel('Class')
plt.xlabel('Province')
plt.show()

# 1993年各省GDP类别分布
print(f'GDP in 1993:\n{q5[:,0]}')

# Beijing’s quintile time series
print(f'Beijing’s quintile time series:\n{q5[0,:]}')
plt.scatter(range(1993,2014), q5[0,:])
plt.show()

# instantiate a Markov object
m5 = pysal.Markov(q5)
print(f'instantiate a Markov object:\n{m5.transitions}')

print(f'the transition probabilities:\n{m5.p}')

print(f'the long run steady state distribution:\n{m5.steady_state}')

print(f'the first mean passage time:\n{pysal.ergodic.fmpt(m5.p)}')

# Spatial Markov######################################################

pci = pci.transpose()
rpci = pci/(pci.mean(axis=0))

w = pysal.open(r"D:\pysal_task\data\GDP_China.swm").read()

w.transform = 'r'
print(w)
sm = pysal.Spatial_Markov(rpci, w, fixed = True, k = 5)
print(sm.p)

for p in sm.P:
    print(p)

print(sm.S)

# for f in sm.F:
    # print(f)

